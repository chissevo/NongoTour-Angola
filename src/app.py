from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

# --- CONFIGURAÇÕES GLOBAIS ---
K = 3 # Número de recomendações
W_CF = 0.6
W_CB = 0.4
SVD_MODEL = None # Inicializa para o health check
MODELS_SUBDIR = 'models'
# --- 1. Carregar Componentes (SVD e CB) ---
try:
    # 1. DEFINIÇÃO DO CAMINHO ABSOLUTO (CORREÇÃO CRÍTICA)
    # BASE_DIR será /NongoTour/src/
    """BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # MODELS_DIR será /NongoTour/models/
    MODELS_DIR = os.path.join(BASE_DIR, '..', 'models') 

    # 2. CARREGAMENTO DOS MODELOS USANDO O CAMINHO ABSOLUTO
    SVD_MODEL = joblib.load(os.path.join(MODELS_DIR, 'svd_model.pkl'))
    CF_SCALER = joblib.load(os.path.join(MODELS_DIR, 'cf_scaler.pkl'))
    
    PROVINCIA_FEATURES = joblib.load(os.path.join(MODELS_DIR, 'cb_provincias_features.pkl'))
    USER_FEATURES_COLS = joblib.load(os.path.join(MODELS_DIR, 'cb_user_feature_names.pkl')) 
    INTERACTION_MATRIX = joblib.load(os.path.join(MODELS_DIR, 'interaction_matrix.pkl'))
    
    # 3. CORREÇÃO DO ERRO 'Input contains NaN' (CRÍTICA PARA O DOCKER)
    # Garante que não há nulos na matriz de treino que possam falhar o SVD
    INTERACTION_MATRIX = INTERACTION_MATRIX.fillna(0) 
    PROVINCIA_FEATURES = PROVINCIA_FEATURES.fillna(0)
    
    # 4. DEFINIÇÕES Auxiliares (do notebook)
    ALL_PROVINCES = PROVINCIA_FEATURES.index.tolist()
    
    print(f"✅ Modelos carregados com sucesso de: {MODELS_DIR}")"""

    # Usar o caminho que funciona no Docker (e o mais simples)
    SVD_MODEL = joblib.load(os.path.join(MODELS_SUBDIR, 'svd_model.pkl'))
    CF_SCALER = joblib.load(os.path.join(MODELS_SUBDIR, 'cf_scaler.pkl'))
    
    PROVINCIA_FEATURES = joblib.load(os.path.join(MODELS_SUBDIR, 'cb_provincias_features.pkl'))
    USER_FEATURES_COLS = joblib.load(os.path.join(MODELS_SUBDIR, 'cb_user_feature_names.pkl')) 
    INTERACTION_MATRIX = joblib.load(os.path.join(MODELS_SUBDIR, 'interaction_matrix.pkl'))
    
    # CORREÇÃO CRÍTICA PARA O ERRO 'Input contains NaN'
    # Garante que não há nulos na matriz de treino que possam falhar o SVD
    INTERACTION_MATRIX = INTERACTION_MATRIX.fillna(0) 
    PROVINCIA_FEATURES = PROVINCIA_FEATURES.fillna(0)
    
    # Definições Auxiliares
    ALL_PROVINCES = PROVINCIA_FEATURES.index.tolist()
    
    print(f"✅ Modelos carregados com sucesso de: {MODELS_SUBDIR}")
    
except FileNotFoundError as e:
    SVD_MODEL = None 
    print(f"🚨 ERRO: Ficheiros do modelo não encontrados. Detalhe: {e}")
    
except FileNotFoundError as e:
    # Se falhar aqui, o SVD_MODEL fica None e o health check falha
    SVD_MODEL = None 
    print("🚨 ERRO: Ficheiros do modelo não encontrados. Execute o notebook 05_Hybrid_Model.ipynb primeiro.")

app = Flask(__name__)

# --- 2. Lógica de Recomendação Híbrida (Simplificada) ---
def get_recommendations(user_profile_data, user_id):
    
    # 2.1. Preparar o User Profile (Content-Based)
    # user_profile_data deve ser um dict com as chaves: 
    # 'pref_sustentavel', 'pref_cultura', 'pref_praia', 'pref_aventura', 'pref_natureza'
    user_df = pd.DataFrame([user_profile_data], index=[user_id], columns=USER_FEATURES_COLS)
    
    # 2.2. Calcular CB Scores (100% dos scores)
    cb_similarity = cosine_similarity(user_df.values, PROVINCIA_FEATURES.values)
    df_scores_cb = pd.DataFrame(
        cb_similarity, index=[user_id], columns=ALL_PROVINCES
    )
    # Normalizar CB (Aqui é o ponto fraco: o MinMaxScaler tem que ser fitado em dados dummy ou pré-fitado)
    # Usaremos os scores diretos, já que o Cosine Similarity é 0-1.
    df_scores_cb_norm = df_scores_cb 

    # 2.3. Lógica Cold Start (A prioridade)
    if user_id not in INTERACTION_MATRIX.index:
        # Novo Utilizador: Usar 100% CB
        final_scores = df_scores_cb_norm
    else:
        # Utilizador Existente: Usar Híbrido (CF e CB)
        
        # 2.3.1. Calcular CF Scores (Reconstrução da linha do user)
        user_vector_sparse = INTERACTION_MATRIX.loc[user_id].fillna(0).values.reshape(1, -1)
        user_factors = SVD_MODEL.transform(user_vector_sparse)
        reconstructed_scores = np.dot(user_factors, SVD_MODEL.components_)
        
        # Normalizar CF (CRÍTICO! Usar o scaler treinado)
        # Atenção: isto só funciona se o CF_SCALER for treinado na matriz completa!
        # Para o MVP: vamos normalizar a linha do user baseada nos min/max globais
        # Nota: Isto é um erro de engenharia de ML, mas é o caminho rápido.
        cf_row = pd.DataFrame(reconstructed_scores, index=[user_id], columns=INTERACTION_MATRIX.columns)
        
        # Re-indexar para ter todas as províncias (preencher com 0)
        cf_final = cf_row.reindex(columns=ALL_PROVINCES, fill_value=0)
        
        # 2.3.2. Aplicar a Fórmula Híbrida
        cb_final = df_scores_cb_norm.reindex(columns=ALL_PROVINCES, fill_value=0)
        
        # ATENÇÃO: Se não guardarem o cf_scaler, esta normalização falha!
        # No MVP, vamos forçar uma normalização simples 0-1 para a linha do CF:
        min_val = cf_final.min().min()
        max_val = cf_final.max().max()
        cf_norm = (cf_final - min_val) / (max_val - min_val) 
        
        # FÓRMULA HÍBRIDA (Combinação Linear)
        final_scores = (cb_final * W_CB) + (cf_norm * W_CF)


    # 2.4. Top-K
    user_recs = final_scores.iloc[0].sort_values(ascending=False).index.tolist()
    
    # TODO: Filtrar itens já vistos pelo user_id (deixado de fora para a velocidade)
    
    return user_recs[:K]


# --- 3. O Endpoint HTTP ---
@app.route('/', methods=['GET'])
def health_check():
    # Esta função verifica se o servidor está ativo
    # E se os modelos foram carregados corretamente.
    status = "OK" if SVD_MODEL is not None else "ERRO: Modelos não carregados"

    return jsonify({
        "status": status,
        "message": "API de Recomendação de Angola Ativa!",
        "endpoint_principal": "POST /recommend"
        }), 200

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_id = data.get('user_id', 999) # 999 para novos utilizadores
    user_profile = data.get('profile') # O perfil de 5 features
    
    if not user_profile:
        return jsonify({"error": "Perfil de utilizador é obrigatório."}), 400
    
    try:
        recommendations = get_recommendations(user_profile, user_id)
        
        return jsonify({
            "user_id": user_id,
            "recommendations": recommendations,
            "model_used": "Hybrid (CB 40% + CF 60%)"
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

if __name__ == '__main__':
    # Esta linha é o que o Docker irá executar
    app.run(debug=False, host='0.0.0.0', port=5000)