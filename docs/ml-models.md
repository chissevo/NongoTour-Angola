[INPUT: Reviews em Texto] -> [1. Sentiment Analysis (NLTK)] -> [user_ratings.csv] | v [INPUT: província_features_v2.csv] | [INPUT: User Activity] -> [2. Clustering (K-Means)] -> [user_profiles.csv] | | | v +----------------------------> [3A. Content-Based Model] | (Cosine Similarity) | | | v v [Scores CB] [3B. Collaborative Filtering] | (SVD / NMF) | | v v [Scores CF] <------------+ | v [4. Hybrid Engine (Logic)] | v [OUTPUT: Recomendações Finais]

# NongoTour: Arquitectura do Sistema de Machine Learning
**Propósito:** Este documento detalha a arquitectura da pipeline de Machine Learning do NongoTour. O objectivo não é um único modelo, mas um **sistema híbrido** que resolve o problema do "Cold Start" e cumpre o objectivo de negócio de promover o turismo sustentável e diversificado.

---

## 1. Visão Geral da Arquitectura (Fluxo de Dados)

O sistema é uma pipeline composta que transforma dados não-estruturados (reviews) em recomendações personalizadas.

---

## 2. Componentes Detalhados da Pipeline

### 2.1. Componente 1: Processamento de Dados (Sentiment Analysis)
* **Objectivo:** Transformar dados não-estruturados (reviews em texto) em dados estruturados (ratings numéricos).
* **Notebook:** `notebooks/03a_Sentiment_Analysis.ipynb`
* **Modelo:** `nltk.sentiment.vader.SentimentIntensityAnalyzer` (VADER)
* **Input:** `data/mock_reviews.csv` (coluna `review_texto`)
* **Processo:**
    1.  O VADER analisa cada review e gera um "score composto" (de -1.0 a +1.0).
    2.  Este score é normalizado e convertido para um rating de 1 a 5.
* **Output:** `data/user_ratings_v2.csv` (colunas: `user_id`, `provincia`, `rating_calculado`)

### 2.2. Componente 2: Descoberta de Perfis (Clustering)
* **Objectivo:** Vamos *descobrir* perfis com base no comportamento e dados demográficos.
* **Notebook:** `notebooks/03b_Clustering.ipynb`
* **Modelo:** `sklearn.cluster.KMeans`
* **Input:**
    1.  Dados demográficos do utilizador (quando disponíveis).
    2.  Dados de actividade (ex: média do `impacto_ambiental` dos locais que visitou, % de reviews sobre "aventura").
* **Processo:**
    1.  O K-Means agrupa os utilizadores em `k` clusters (ex: k=4).
    2.  Analisamos estes clusters e damo-lhes "personas" (ex: Cluster 0 = "Eco-Aventureiro", Cluster 1 = "Turista de Baixo Custo").
* **Output:** `data/user_profiles.csv` (colunas: `user_id`, `profile_cluster`)

---

## 3. Os Modelos de Recomendação

### 3.1. Modelo A: Content-Based Filtering (CB)
* **Propósito:** Recomendar com base em *features* do item e do perfil do utilizador. Este é o nosso motor principal para o **problema do "Cold Start"**.
* **Técnica:** Similaridade de Cosseno (Cosine Similarity).
* **Inputs:**
    1.  **Perfil do Utilizador:** `data/user_profiles.csv` (o *output* do Clustering).
    2.  **Perfil do Item:** `data/provincia_features_v2.csv` (os novos dados com `acessibilidade`, `impacto_ambiental`, `custo_medio`, etc.).
* **Ponto Cego:** Não descobre gostos "escondidos" (serendipidade). Se um utilizador está no cluster "Praia", só recomendará praia.

### 3.2. Modelo B: Collaborative Filtering (CF)
* **Propósito:** Recomendar com base no *comportamento colectivo*. ("Pessoas como você, que gostaram de Malanje, também gostaram de Cabinda").
* **Técnica:** Factorização de Matrizes (ex: `sklearn.decomposition.NMF` ou `SVD`).
* **Input:** `data/user_ratings_v2.csv` (a matriz `user-item` gerada pelo Sentiment Analysis).
* **Processo:** O modelo "aprende" factores latentes (características escondidas) para utilizadores e províncias.
* **Ponto Cego:** **Totalmente inútil para novos utilizadores** (Cold Start). Não consegue recomendar itens que não tenham ratings.

---

## 4. A Estratégia Híbrida (O "Cérebro")

Nenhum dos modelos é suficiente sozinho. O sistema NongoTour **tem** de ser híbrido.

* **Propósito:** Obter o melhor dos dois mundos: a relevância do CF e a segurança do CB contra o "Cold Start".
* **Lógica de Hibridização:** Ponderada com *switching*.

```python
def get_recommendations(user_id, k=5):
    
    # Contar os ratings do utilizador
    num_ratings = get_user_rating_count(user_id)
    
    # Lógica de "Switching" para Cold Start
    if num_ratings < 3:
        # Utilizador é novo. CF é inútil.
        # Usar 100% Content-Based
        final_scores = get_content_based_scores(user_id)
    else:
        # Utilizador tem historial. Usar Híbrido Ponderado.
        scores_cb = get_content_based_scores(user_id)
        scores_cf = get_collaborative_filtering_scores(user_id)
        
        # Dar mais peso ao CF, pois aprende com o comportamento
        final_scores = (scores_cf * 0.6) + (scores_cb * 0.4)
        
    # Retornar o Top-K das pontuações finais
    return final_scores.nlargest(k)