# 🧭 Plano de Implementação — NongoTour Angola

## 1. Introdução
O presente plano de implementação descreve as etapas técnicas, metodológicas e operacionais para o desenvolvimento da aplicação **NongoTour Angola**, uma plataforma inteligente de recomendação de destinos turísticos sustentáveis baseada em Machine Learning.
O objetivo é promover a descentralização do turismo e impulsionar o desenvolvimento económico equitativo em Angola.

---

## 2. Estrutura do Projeto
O projeto está organizado em quatro módulos principais:

- **Módulo de Dados:** Recolha, tratamento e armazenamento dos dados turísticos.
- **Módulo de Análise e Machine Learning:** Preparação, modelagem, validação e avaliação dos dados.
- **Módulo Web:** Interface interativa (frontend/backend) para recomendação e visualização de destinos.
- **Módulo de Monitorização:** Avaliação do impacto do sistema e indicadores ligados aos ODS 8, 11 e 12.

---

## 3. Etapas de Implementação

### Fase 0 — Configuração, Dados Mock e Baseline (Semana 1)
O objetivo é preparar o ambiente de desenvolvimento e criar um "baseline" para permitir o início imediato do trabalho de ML, conforme as recomendações.

- Configuração do repositório GitHub (`README.md`, `requirements.txt`).
- Criação de **datasets mock** (fictícios) `destinos_mock.csv` e `avaliacoes_mock.csv` para permitir o desenvolvimento paralelo.
- **Resultado:** Notebook `00_Modelo_Baseline.ipynb` (implementa um modelo simples, ex: "recomendar os 10 mais populares", para servir de base de comparação).

---

### Fase 1 — Planeamento e Preparação de Dados
- Identificação das fontes (INFORTUR, INE, TripAdvisor, etc.)
- Criação do esquema de dados (CSV ou Base SQL)
- Tratamento, limpeza e uniformização dos dados **reais**.
- Documentação no ficheiro `preparacao_dados.md`

**Resultado esperado:** Dataset final `turismo_angola_completo.csv` pronto para análise.

---

### Fase 2 — Análise Exploratória (EDA)
- Estudo de correlações e padrões entre variáveis (destinos, avaliações, acessibilidade) - *inicialmente com dados mock, depois com dados reais*.
- Visualização de distribuições por província
- Identificação de variáveis-chave para modelagem

**Ferramentas:** Python (Pandas, Matplotlib, Seaborn, Plotly)
**Saída:** Notebook `01_Analise_Exploratoria_EDA.ipynb`

---

### Fase 3 — Engenharia de Recursos
- Criação de variáveis derivadas:
  - Índice de Sustentabilidade do Destino
  - Índice de Inclusão Comunitária
  - Escore de Acessibilidade
- Normalização e codificação de dados para uso em modelos ML.

**Saída:** `dataset_pronto_modelagem.csv`

---

### Fase 4 — Modelagem e Validação
- **Sistemas de Recomendação:** Filtragem colaborativa e híbrida
- **Clustering:** Segmentação de perfis de turistas
- **Análise de Sentimentos:** Classificação de avaliações textuais
- **Validação Cruzada (k-fold)** e **Split Temporal**

**Métricas:**
- RMSE / MAE → Precisão das previsões
- F1 / Recall / Precision → Análise de sentimento
- Silhouette Score → Clustering

---

### Fase 5 — Desenvolvimento do Protótipo
- **Backend:** API em **Laravel** integrando modelos ML via Python
- **Frontend:** Interface em **React + Inertia.js**
- **Containerização (Pre-Cloud):** A aplicação (Laravel + Python API) será "dockerizada" para garantir paridade total entre os ambientes de desenvolvimento, testes (Staging) e produção na nuvem.
- **Funcionalidades principais:**
  - Recomendação personalizada
  - Filtros por tipo de destino
  - Mapa interativo dos destinos emergentes
  - Dashboard de impacto (ODS 8, 11, 12)

---

### Fase 6 — Testes, Avaliação e Staging
- Testes unitários e de integração
- Testes de usabilidade (UX/UI)
- **Implantação em Staging (Pré-Produção):** A aplicação será implementada num ambiente de nuvem de testes (*Staging*) para validar o desempenho, a segurança e a integração dos serviços em condições reais.
- Avaliação da eficácia das recomendações com dados simulados

---

### Fase 7 — Lançamento (Produção) e Monitorização Contínua
- **Implantação em Produção:** Lançamento da versão estável da aplicação no ambiente de nuvem principal, acessível aos utilizadores finais.
- **Monitorização de Desempenho e Métricas de Impacto:**
  - Implementação de métricas de impacto:
    - Percentagem de recomendações para destinos emergentes
    - Redução da concentração turística em Luanda
  - Recolha de feedback dos utilizadores e comunidades locais
  - Ajuste periódico dos modelos ML com novos dados

---

## 4. Cronograma de Implementação (Exemplo)
| Fase | Descrição | Duração | Período |
|------|------------|----------|----------|
| 0 | Configuração e Baseline | 1 semana | Out 2025 |
| 1 | Preparação de Dados Reais | 3 semanas | Out–Nov 2025 |
| 2 | EDA e Engenharia de Recursos | 4 semanas | Nov–Dez 2025 |
| 3 | Modelagem e Validação | 5 semanas | Jan–Fev 2026 |
| 4 | Desenvolvimento do Protótipo | 6 semanas | Fev–Mar 2026 |
| 5 | Testes e Avaliação (Staging) | 3 semanas | Abr 2026 |
| 6 | Lançamento e Monitorização | Contínuo | Mai–Jun 2026 |

---

## 5. Recursos Necessários
- **Humanos:** Cientistas de dados, programadores web, analistas de turismo e designers UX/UI.
- **Tecnológicos:** Python, Jupyter, Laravel, React, PostgreSQL, Docker.
- **Ambiente de Nuvem:** Definição da plataforma de cloud (ex: **AWS, Google Cloud, Azure, ou DigitalOcean**) para os ambientes de *Staging* (Testes) e *Produção*.
  - **Serviços-chave:** (ex: Base de Dados Gerida como **RDS/Cloud SQL**, serviço de container como **ECS/AppRunner**, e *storage* como **S3/Cloud Storage** para guardar os modelos ML).
- **Dados:** Fontes oficiais (INFORTUR, INE), APIs abertas e dados recolhidos por inquérito.

---

## 6. Indicadores de Sucesso
| Objetivo | Indicador | Meta |
|-----------|------------|------|
| Inclusão de destinos emergentes | Percentagem de recomendações fora dos grandes centros | ≥ 25% |
| Sustentabilidade | Índice médio de sustentabilidade dos destinos recomendados | ≥ 70% |
| Satisfação dos utilizadores | Taxa de aceitação das recomendações | ≥ 80% |

---

## 7. Conclusão
O presente plano define uma rota clara para o desenvolvimento, implantação e validação do **NongoTour Angola**, garantindo que o sistema recomende destinos turísticos de forma **inteligente, sustentável e inclusiva**, alinhando-se com os **Objetivos de Desenvolvimento Sustentável (ODS) 8, 11 e 12**.