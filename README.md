<img src="NongoTour Angola.png" width="998" height="472">

# 🚀 NongoTour: Turismo Inteligente para um Crescimento Inclusivo em Angola

**NongoTour** é uma aplicação web de recomendação de destinos turísticos em Angola. Utilizando Machine Learning, a plataforma direciona os turistas com base nas suas preferências, com o objetivo de promover a descentralização do turismo e impulsionar o desenvolvimento económico equitativo.

Este projeto responde aos desafios identificados na nossa **[Nota Conceitual](docs/nota_conceitual.md)** e segue o cronograma do nosso **[Plano de Implementação](docs/plano_implementacao.md)**.


## 🗂️ Estrutura do Projeto

Abaixo está a organização dos diretórios e ficheiros principais do projeto **NongoTour**:

```
/NongoTour/
    |
    |-- 📂 data/
        |-- provincia_features_MVP.csv
    |   |-- provincia_features_v2.csv
    |   |-- mock_reviews.csv
    |   |-- user_features_MVP.csv
    |   |-- user_interactions_MVP
    |
    |-- 📂 docs/
    |   |-- ml-models.md
    |   |-- revisao_literatura_africa.md
    |   |-- plano_implementacao.md
    |   |-- nota_conceitual
    |-- 📂 models/
    |   |--cb_provincias_features.pkl
    |   |--cb_user_feature_names.pkl
    |   |--cf_scaler.pkl
    |   |--interaction_matrix.pkl
    |   |--svd_model.pkl   (Modelo de treino)
    |-- 📂 notebooks/
    |   |-- 01_Analise_Exploratoria_EDA.ipynb
    |   |-- 02_Baseline_Model.ipynb
    |   |-- 03_Content_Based_Model.ipynb
    |   |-- 03a_Sentiment_Analysis.ipynb
    |   |-- 04_Collaborative_Filtering.ipynb
    |   |-- 05_Hybrid_Model.ipynb
    |-- 📂 src/
    |   |-- app.py (Nossa API)
    |-- .dockerignore (Informações que devem ser ignoradas no nosso docker container)
    |-- Dockerfile (Regras para a criação do nosso docker container)
    |-- README.md
    |-- requirements.txt
```

## 1. O Problema: A Concentração do Turismo
*(Esta secção vem da sua `nota_conceitual.md`)*

A análise dos dados de turismo em Angola revela uma forte concentração de turistas e receitas em províncias "estabelecidas", como Luanda e Benguela.

* **Destinos Estabelecidos (ex: Luanda):** Recebem a maioria dos visitantes, sobrecarregando a infraestrutura local.
* **Destinos Emergentes (ex: Bengo, Moxico, Lundas):** Possuem um vasto potencial cultural e natural, mas recebem uma fração do fluxo turístico, limitando o seu desenvolvimento económico.

## 2. A Solução e o Alinhamento com os ODS
*(Esta secção também vem da sua `nota_conceitual.md`)*

O NongoTour utiliza um modelo de recomendação para sugerir ativamente destinos emergentes a perfis de turistas compatíveis, criando um impacto direto em três ODS principais:

* **🌍 ODS 8 (Trabalho Digno e Crescimento Económico):** Ao canalizar receitas para novas províncias, estimulamos a criação de empregos locais.
* **🏙️ ODS 11 (Cidades e Comunidades Sustentáveis):** Ao aliviar a pressão turística de Luanda, reduzimos a sobrecarga da infraestrutura urbana.
* **🌿 ODS 12 (Consumo e Produção Responsáveis):** Promovemos um "consumo" de turismo mais sustentável, focado em produtos e culturas locais.

## 3. 📊 Análise e Simulação de Impacto (Baseline)

Para validar a nossa abordagem, analisámos o dataset `turismo_angola_completo.csv` para estabelecer uma linha de base (2024) e simular o impacto do NongoTour (2025).

A análise completa, código Python e preparação de dados (baseado no documento `preparacao_dados.md`) podem ser encontrados no notebook: **[notebooks/01_Analise_Exploratoria_EDA.ipynb]**

#### Tabela 1: Linha de Base (Baseline 2024)
| Indicador | Valor (2024) |
| :--- | :--- |
| Total de Turistas | 854.000 |
| Concentração em Luanda | 16.04% |
| Quota (5 Prov. Emergentes) | 13.70% |

#### Tabela 2: Simulação de Impacto (2025)
| Indicador | Baseline (2024) | Simulado (2025) | Mudança |
| :--- | :--- | :--- | :--- |
| Concentração em Luanda | 16.04% | 14.91% | **-1.13 pts** |
| Quota (5 Prov. Emergentes) | 13.70% | 16.38% | **+2.68 pts** |

#### Tabela 3: Resumo do Impacto nos ODS
| ODS | Objetivo Específico | Indicador-Chave (KPI) | Resultado da Simulação |
| :--- | :--- | :--- | :--- |
| **ODS 8** | Distribuir riqueza | Aumento da Quota (Emergentes) | **+2.68 pontos** |
| **ODS 11** | Reduzir pressão urbana | Redução da Concentração (Luanda) | **-1.13 pontos** |
| **ODS 12** | Promover turismo local | Aumento da Quota (Emergentes) | **+2.68 pontos** |

## 4. 🤖 Metodologia de Machine Learning

O núcleo do NongoTour será um **Sistema de Recomendação Híbrido** (combinando filtragem baseada em conteúdo e colaborativa).

#### Métricas de Avaliação
Para avaliar a performance do nosso modelo, usaremos:
* **Métricas de Recomendação (Offline):**
    * **RMSE (Root Mean Square Error):** Para prever *ratings* (classificações) que um utilizador daria a um destino.
    * **Precisão (Precision) e Recall@k:** Para avaliar a relevância dos *top-k* destinos recomendados.
    * **F1-Score:** A média harmónica de Precisão e Recall.
* **Métricas de Negócio (Online):**
    * `% de destinos emergentes recomendados` (Métrica de Diversidade)
    * `Taxa de Conversão` (Cliques nas recomendações)

#### Métodos de Validação
Usaremos **Cross-Validation (Validação Cruzada)** para garantir que o modelo generaliza bem. Devido à natureza temporal dos dados de turismo, também exploraremos um **Split Temporal** (treinar com dados antigos, testar com dados mais recentes).

## 5. 📚 Revisão de Literatura

Uma revisão detalhada da literatura, focada em sistemas de recomendação para turismo e experiências de turismo sustentável no contexto Africano, pode ser encontrada no nosso documento dedicado: **[docs/revisao_literatura_africa.md]**.

## 6. 🛠️ Como Executar o Projeto

#### Fonte de Dados
Os dados utilizados neste projeto (reais e fictícios) encontram-se na pasta `/data/`.
* `turismo_angola_completo.csv`: Dados agregados de turismo por província.
* `mock_user_preferences.csv`: Dados fictícios de preferências de utilizadores para testes.

#### Instalação
1.  Clone este repositório:
    ```bash
    git clone https://github.com/chissevo/NongoTour-Angola.git
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Explore a análise de dados no Jupyter Notebook:
    ```bash
    jupyter notebook notebooks/01_Analise_Exploratoria_EDA.ipynb
    ```