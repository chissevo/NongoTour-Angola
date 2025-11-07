# Nota Conceitual: NongoTour Angola

O presente **Projeto**, intitulado NongoTour Angola, propõe o desenvolvimento de uma aplicação inteligente que utilize Machine Learning para
recomendar destinos turísticos em Angola com base em preferências dos usuários, dados de impacto ambiental, e potencial económico local, incentivando práticas de turismo sustentável e inclusivo.

**Data:** 20 de Outubro de 2025

**Membros da Equipa:** 
    
    1º.  Alberto Carlos De Jesus  Pessela 
    2º.  Ataide Garrett  Kapinala
    3º.  Maria Emília Caculo José
    4º.  Joao da Silva Antônio
    5º.  José Poba
    6º.  Sérgio Chisevo
    
---

### 1. Visão Geral do projecto

O setor do turismo em Angola apresenta um grande potencial de crescimento,
mas enfrenta desafios relacionados à má distribuição dos fluxos turísticos, à falta de dados integrados e à pouca visibilidade de destinos emergentes
fora dos grandes centros.

![Distribuição de Turista por Províncias](../files/Visitas%20Por%20Provincias.png)


Além disso, muitas comunidades locais não beneficiam equitativamente das
receitas do turismo, e a ausência de estratégias sustentáveis tem contribuído para a degradação ambiental em algumas áreas.


Diante desse contexto, surge a necessidade de usar tecnologias inteligentes
para analisar, prever e recomendar destinos turísticos que promovam
sustentabilidade, inclusão social e equilíbrio regional.

Diante deste problema formulamos o problema de pesquisa da seguinte forma:

**Como a aplicação de técnicas de Machine Learning pode contribuir para promover o turismo sustentável e equitativo em Angola, através da análise e recomendação inteligente de destinos turísticos?**

### 2. Objectivos

#### 2.1. Objectivo Geral
Desenvolver uma aplicação inteligente denominada NongoTour Angola, baseada em técnicas de Machine Learning, capaz de recomendar destinos turísticos sustentáveis e promover a equidade na distribuição dos fluxos turísticos em Angola.

#### 2.2. Objectivos Específicos
* Recolher dados turísticos de Angola, incluindo informações sobre destinos, avaliações, acessibilidade, impacto ambiental e perfil dos turistas. 
* Analisar os dados recolhidos utilizando métodos estatísticos e exploratórios (EDA) para identificar padrões e fatores determinantes nas escolhas turísticas.
* Aplicar algoritmos de Machine Learning, como sistemas de recomendação (Recommender Systems), agrupamento (Clustering) e análise de sentimento (Sentiment Analysis), para gerar previsões e recomendações inteligentes.
* Desenvolver um protótipo funcional da aplicação SmartTour Angola (versão web ou mobile) integrando os modelos de Machine Learning ao
sistema de recomendação de destinos.
* Garantir que o sistema de recomendação promova a inclusão e sustentabilidade, estabelecendo uma meta de que pelo menos 25% das recomendações geradas sejam para destinos emergentes (fora dos grandes centros) ou geridos por comunidades locais.
* Propor diretrizes estratégicas para o uso de tecnologias inteligentes na formulação de políticas públicas de turismo sustentável em Angola.

### 3. História
O turismo em Angola tem um potencial inexplorado, mas a sua estrutura atual é altamente centralizada, sobrecarregando províncias populares e negligenciando regiões com grande valor ecológico. Esta concentração é insustentável a longo prazo devido à pressão ambiental que impõe.

A abordagem de Machine Learning e Análise de Dados é crucial porque as soluções tradicionais (gestão manual ou baseada em relatórios estáticos) carecem da capacidade de processar e correlacionar grandes volumes de dados (fluxo de visitantes, dados geográficos e indicadores ecológicos) de forma dinâmica.

### 4. Metodologia Proposta
O projeto seguirá uma metodologia de Ciência de Dados, dividida em:
1. **Recolha e Preparação de Dados:** A recolha de dados será realizada a partir de fontes primárias e secundárias,
incluindo: Bases de dados públicas (Ex: INFORTUR, Ministério da Cultura e Turismo, Instituto Nacional de Estatística).
2. **Engenharia de Recursos:** Criação de variáveis relevantes, como um "índice de sustentabilidade" para cada local.

3. **Modelagem:** Exploração de algoritmos de Machine Learning (ex: filtragem colaborativa, sistemas baseados em conteúdo, ou modelos híbridos) para gerar as recomendações.

4.3. **Modelagem e Validação de Modelos:** A modelagem explorará vários algoritmos, e cada um será avaliado com métricas apropriadas:

* ***Sistemas de Recomendação*** (Filtragem Colaborativa/Híbrida): A precisão das previsões de rating será medida usando RMSE (Root Mean Square Error) e MAE (Mean Absolute Error).

* ***Análise de Sentimento*** (Classificação): A capacidade de classificar corretamente as avaliações será medida por Precisão, Recall e F1-Score.

* ***Agrupamento*** (Clustering) de Turistas: A qualidade dos segmentos de perfis será avaliada usando o Silhouette Score.

    Para garantir a robustez dos modelos e evitar overfitting, usaremos a técnica de Validação Cruzada (k-fold Cross-Validation). Dado que os padrões de turismo mudam, também exploraremos um split temporal (treinar com dados antigos, testar com dados mais recentes).

4.4 **Prototipagem e Avaliação:** Desenvolvimento de uma interface para visualização das recomendações e medição da sua eficácia.

### 5. Resultados Esperados e Impacto
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
