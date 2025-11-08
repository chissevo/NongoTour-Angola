# Plano de Implementação: NongoTour

Este documento detalha o plano de implementação faseado para o projeto NongoTour, desde a estruturação inicial até à entrega final.

## Fase 0: Estruturação e Ambiente (1ª Semana)

O objetivo é "preparar o terreno". O foco é criar a estrutura para a equipa trabalhar de forma organizada antes de iniciar a modelagem.

### 🎯 Objetivo Principal
Montar o ambiente de desenvolvimento, criar os artefactos iniciais do projeto e integrar o feedback da nota conceitual.

### 📋 Tarefas Concretas
1.  **Configuração do GitHub:**
    * Criação do repositório central.
    * Redação do `README.md` principal (baseado na Nota Conceitual).
    * Criação do ficheiro `requirements.txt` inicial (com `pandas`, `notebook`, `scikit-learn`, `matplotlib`).
    * Definição da estrutura de pastas (ex: `/data`, `/notebooks`, `/src`).
2.  **Criação dos Dados Mock:**
    * Desenvolver e carregar os datasets fictícios (ex: `destinos_mock.csv`, `avaliacoes_mock.csv`) na pasta `/data`, conforme recomendação.
3.  **Revisão e Baseline:**
    * **Pesquisa:** Expandir a secção de Revisão de Literatura (ou História) com casos de estudo africanos em turismo sustentável.
    * **ML:** Criar o primeiro notebook (`notebooks/01_EDA.ipynb`) que carrega e explora os **dados mock**.
4.  **Atualização da Documentação:**
    * Atualizar a `nota_conceitual.md` para refletir os KPIs de ODS e as métricas de ML detalhadas (RMSE, F1-Score, etc.).

---

## Fase 1: Coleta de Dados e Baseline (Semanas 2-3)

O trabalho divide-se: uma equipa foca-se nos dados reais enquanto a outra cria um primeiro modelo funcional (com dados mock) para servir de termo de comparação.

### 🎯 Objetivo Principal
Obter os primeiros dados reais e estabelecer um "Modelo Baseline" para futuras comparações.

### 📋 Tarefas Concretas
1.  **Coleta de Dados Reais:**
    * Iniciar a recolha de dados das fontes identificadas (INFORTUR, INE, etc.).
    * Iniciar o processo de limpeza e pré-processamento (Data Cleaning) dos dados reais.
2.  **Modelo Baseline (com Dados Mock):**
    * Criar o notebook `notebooks/02_Baseline_Model.ipynb`.
    * Implementar o modelo mais simples possível (ex: "Recomendar os 10 destinos com *rating* médio mais alto").
    * Implementar as funções de avaliação (Precisão, Recall, RMSE) que servirão para todos os modelos.
3.  **Engenharia de Recursos (Inicial):**
    * Definir e calcular (mesmo que de forma simulada) o "índice de sustentabilidade" para os destinos.

---

## Fase 2: Modelagem e Experimentação (Semanas 4-6)

Esta é a fase central de Machine Learning. O objetivo é desenvolver e testar modelos que sejam comprovadamente melhores que o *baseline*.

### 🎯 Objetivo Principal
Desenvolver, treinar e validar os modelos de Machine Learning propostos.

### 📋 Tarefas Concretas
1.  **Desenvolvimento dos Modelos:**
    * Implementar os algoritmos de recomendação (ex: Filtragem Colaborativa, Baseada em Conteúdo).
    * Implementar modelos auxiliares (Análise de Sentimento, Agrupamento de turistas).
2.  **Treino e Validação:**
    * Treinar os modelos (idealmente com dados reais, se já disponíveis).
    * Aplicar rigorosamente os métodos de validação (Cross-Validation, split temporal).
    * Gerar e salvar as métricas de desempenho de cada modelo.
3.  **Seleção e Ajuste (Tuning):**
    * Comparar as métricas de todos os modelos contra o *baseline*.
    * Selecionar o(s) modelo(s) com melhor desempenho para a prototipagem.
    * Afinar os hiperparâmetros do modelo vencedor.

---

## Fase 3: Prototipagem e Integração (Semanas 7-8)

Um modelo num notebook não é um produto. Esta fase foca-se em tornar o modelo acessível através de uma aplicação.

### 🎯 Objetivo Principal
Criar um protótipo funcional (web ou mobile) que consome o modelo de ML treinado.

### 📋 Tarefas Concretas
1.  **Backend (API):**
    * Salvar o modelo treinado (ex: num ficheiro `.pkl` ou `.joblib`).
    * Criar uma API simples (ex: usando Flask ou FastAPI) que recebe um pedido (ex: `user_ID`) e devolve uma lista de recomendações do modelo.
2.  **Frontend (UI):**
    * Desenvolver a interface de utilizador (protótipo) onde o utilizador pode inserir preferências ou ver recomendações.
3.  **Testes de Integração:**
    * Garantir que o fluxo completo (Frontend -> API -> Modelo -> Recomendação) funciona corretamente.

---

## Fase 4: Avaliação e Entrega (Semanas 9-10)

Foco em testar o impacto (ODS) e preparar a entrega final do projeto.

### 🎯 Objetivo Principal
Avaliar o impacto real do protótipo face aos objetivos de sustentabilidade (ODS) e preparar a apresentação final.

### 📋 Tarefas Concretas
1.  **Avaliação de Impacto (ODS):**
    * Executar simulações no protótipo para medir os KPIs de ODS definidos na Fase 0 (ex: "Qual a % de destinos emergentes recomendados?").
2.  **Conclusão e Apresentação:**
    * Redigir as "diretrizes estratégicas" para políticas públicas (um dos objetivos do projeto).
    * Preparar a apresentação final e o "pitch" do NongoTour.
    * Garantir que o repositório GitHub está limpo, documentado e que o código é executável.

---

## 🤝 Gestão da Equipa e Divisão de Tarefas

Com 6 membros, sugere-se uma divisão em frentes de trabalho:

* **Frente de Dados e Pesquisa (2 membros):** Foco na Fase 0 (Revisão Lit.), Fase 1 (Coleta e Limpeza de Dados) e Fase 2 (Eng. de Recursos).
* **Frente de ML/Modelagem (2 membros):** Foco na Fase 1 (Baseline), Fase 2 (Modelagem/Validação) e Fase 3 (API).
* **Frente de Produto/Frontend (2 membros):** Foco na Fase 3 (Frontend/UI) e Fase 4 (Testes de Impacto ODS, Apresentação).

Recomenda-se uma sincronização semanal (stand-up) de 15 minutos para partilhar progressos e bloqueios.