# Plano de Preparação de Dados e Engenharia de Recursos

## 1. Visão Geral
A fase de **Preparação de dados e Engenharia de Recursos** é essencial para garantir a qualidade dos modelos de Machine Learning no nosso Projecto *NongoTour Angola*.  
Nesta etapa, os dados turísticos e ambientais de Angola serão: **recolhidos, limpos, explorados e transformados** para permitir a análise de padrões e a construção de sistemas de recomendação.  
Essa preparação assegura que o modelo tenha **informações consistentes, relevantes e representativas** da realidade turística angolana.

---

### 2. Fontes de Dados Potenciais

* **Dados Geográficos e de Pontos de Interesse (POIs):**
    * **Instituto Nacional de Estatística (INE Angola)** – fluxos turísticos por província.
    * **Ministério do Turismo e Ambiente** - Áreas de conservação, fragilidade ecológica.
    * **OpenStreetMap e GeoBoundaries** - Coordenadas e mapas geográficos.

    ### Pré-processamento inicial
    * Conversão dos ficheiros para formato `.csv` e `.json`.  
    * Padronização de nomes de colunas e unidades.  
    * Integração de datasets com `pandas.merge()`.
    
    ```python
        import pandas as pd

        turismo = pd.read_csv("dados_turismo.csv")
        ambiente = pd.read_csv("dados_ambiente.csv")

        dados = pd.merge(turismo, ambiente, on="provincia", how="inner")
        dados.head() 
    ```

### 3. Limpeza de Dados 
As principais operações de limpeza incluíram:

* Remoção de valores ausentes (NaN) com imputação pela média ou mediana;
* Exclusão de duplicados;
* Tratamento de valores extremos (IQR);
* Padronização dos tipos de dados.
    
    ```python
        dados['visitantes_ano'].fillna(dados['visitantes_ano'].median(), inplace=True)
        dados.drop_duplicates(inplace=True)
        Q1 = dados['impacto_ecologico'].quantile(0.25)
        Q3 = dados['impacto_ecologico'].quantile(0.75)
        IQR = Q3 - Q1
        dados = dados[~((dados['impacto_ecologico'] < (Q1 - 1.5 *IQR)) |
                       (dados['impacto_ecologico'] > (Q3 + 1.5 * IQR)))]

### 4. Análise Exploratória de Dados (EDA)
A EDA permitiu compreender o comportamento do turismo por província, sazonalidade e impacto ambiental.
Foram geradas visualizações para:
    
* Número de visitantes por província.
* Correlação entre fluxo turístico e impacto ambiental.
* Mapa geográfico dos destinos mais visitados.
    ```python
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10,6))
    sns.barplot(data=dados, x='provincia', y='visitantes_ano')
    plt.xticks(rotation=45)
    plt.title("Número de Visitantes por Província em Angola")
    plt.show()
### Principais insights:
+ As províncias de Luanda, Benguela, Huambo e Cabinda concentram >60% dos visitantes.
+ Regiões como Namibe e Malanje têm alto potencial ecológico e baixa    exploração turística.

+ Correlação positiva entre infraestrutura e volume de visitantes.
![Percentagem de visitantes por Províncias](../files/Percentagem%20de%20Visitantes.png)

### 5. Engenharia de Recursos
Serão criadas novas variáveis (features) para melhorar a performance dos modelos:

+ indice_sustentabilidade = (avaliacao_media * infraestrutura) / impacto_ecologico

+ densidade_turistica = visitantes_ano / area_provincia_km2

+ categoria_turismo (Ecológico, Cultural, Urbano, etc.)
    ```python
        dados['indice_sustentabilidade'] = (
        dados['avaliacao_media'] * dados['infraestrutura'] / dados['impacto_ecologico'])
    ```
### 6. Transformação de Dados

Serão aplicadas técnicas de normalização e codificação:
```python
    from sklearn.preprocessing import MinMaxScaler, LabelEncoder

    scaler = MinMaxScaler()
    dados[['visitantes_ano','indice_sustentabilidade']] = scaler.fit_transform(
    dados[['visitantes_ano','indice_sustentabilidade']])

    encoder = LabelEncoder()
    dados['categoria_turismo'] = encoder.fit_transform(dados['categoria_turismo'])
```
---