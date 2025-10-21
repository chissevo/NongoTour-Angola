# Plano de Preparação de Dados e Engenharia de Recursos

## 1. Visão Geral
A fase de **Preparação de dados e Engenharia de Recursos** é essencial para garantir a qualidade dos modelos de Machine Learning no nosso Projecto *OmaholaTour Angola*.  
Nesta etapa, os dados turísticos e ambientais de Angola serão: **recolhidos, limpos, explorados e transformados** para permitir a análise de padrões e a construção de sistemas de recomendação.  
Essa preparação assegura que o modelo tenha **informações consistentes, relevantes e representativas** da realidade turística angolana.

---

### 2. Fontes de Dados Potenciais

* **Dados Geográficos e de Pontos de Interesse (POIs):**
    * **Instituto Nacional de Estatística (INE Angola)** – fluxos turísticos por província.
    * **Ministério do Turismo e Ambiente** - Áreas de conservação, fragilidade ecológica.
    * **OpenStreetMap e GeoBoundaries** - Coordenadas e mapas geográficos.

    ### Pré-processamento inicial
    1. * Conversão dos ficheiros para formato `.csv` e `.json`.  
    2. * Padronização de nomes de colunas e unidades.  
    3. * Integração de datasets com `pandas.merge()`.

    ```python
        import pandas as pd

        turismo = pd.read_csv("dados_turismo.csv")
        ambiente = pd.read_csv("dados_ambiente.csv")

        dados = pd.merge(turismo, ambiente, on="provincia", how="inner")
        dados.head()

### 3. Limpeza de Dados 
As principais operações de limpeza incluíram:

    **Remoção de valores ausentes (NaN) com imputação pela média ou mediana;

    **Exclusão de duplicados;

    **Tratamento de valores extremos (IQR);

    **Padronização dos tipos de dados.
