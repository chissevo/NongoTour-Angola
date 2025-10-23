# Plano de Implementação do Projeto NongoTour Angola

**1. Objetivo Geral**
Desenvolver uma aplicação inteligente denominada
NongoTour Angola, baseada em técnicas de Machine Learning, capaz de recomendar destinos turísticos sustentáveis e promover a equidade na distribuição dos fluxos turísticos em Angola.
Etapa	Descrição	Ferramentas / Tecnologias	Duração (estimada)	Responsável

1. Coleta de Dados	Recolha de dados turísticos, ambientais e geográficos (INE, Ministério do Turismo, OpenStreetMap).	Python (Pandas), APIs, CSV	2 dias	Maria José
2. Limpeza e Preparação de Dados	Tratamento de dados ausentes, normalização, padronização de colunas e integração de datasets.	Pandas, NumPy	2 dias	Alberto Pessela
3. Análise Exploratória de Dados (EDA)	Exploração visual e estatística dos dados. Criação de gráficos e correlações.	Matplotlib, Seaborn, Plotly	2 dias	Alberto Pessela
4. Engenharia de Recursos (Features)	Criação de novas variáveis: índice de sustentabilidade, densidade turística, categoria de destino.	Pandas, Scikit-learn	2 dias	Sérgio Chissevo
5. Modelagem de Machine Learning	Aplicação de algoritmos de clusterização (K-Means), regressão e recomendação.	Scikit-learn, TensorFlow	2 dias	Sérgio Chissevo
6. Desenvolvimento da Interface	Criação do protótipo web (ou desktop) para visualização de recomendações.	Flask / Streamlit / React	2 dias	João António
7. Visualização e Dashboards	Desenvolvimento de painéis interativos com mapas e indicadores.	Plotly, GeoPandas, Folium	1 dia	José Poba
8. Testes e Validação	Validação cruzada dos modelos e testes de desempenho da aplicação.	Scikit-learn, Pytest	1 dia	Equipe completa
9. Relatórios e Apresentação Final	Elaboração de relatórios e pitch de apresentação.	Jupyter, PowerPoint	1 dia	Ataíde Kapinala

3. Linha do Tempo (Cronograma Geral)
Dias 1–3  → Coleta e limpeza de dados  
Dias 4–5  → Análise exploratória e engenharia de recursos  
Dias 6–7  → Modelagem de aprendizado de máquina  
Dias 8–9  → Desenvolvimento da interface e dashboards  
Dia 10    → Testes, relatório final e apresentação

4. Pilha de Tecnologias
Categoria	Ferramentas
Linguagens	Python, JavaScript
Bibliotecas de ML	Pandas, NumPy, Scikit-learn, TensorFlow
Visualização	Matplotlib, Seaborn, Plotly, GeoPandas, Folium
Framework Web/App	Flask, Streamlit ou React
Base de Dados	CSV, SQLite ou MongoDB
Ambiente de Desenvolvimento	Jupyter Notebook, VS Code, Google Colab
Controle de Versão	GitHub
Infraestrutura	Docker, Render ou AWS (para deploy futuro)


5. Marcos (Metas)
M1: Coleta e validação dos dados concluída
M2: Modelo de Machine Learning funcional e validado
M3: Interface interativa desenvolvida
M4: Relatórios e apresentação final preparados
6. Desafios e Estratégias de Mitigação
Desafio	Estratégia de Mitigação
Dados incompletos ou inconsistentes	Uso de fontes secundárias e interpolação estatística
Desequilíbrio nos dados turísticos	Aplicação de técnicas de resampling e normalização
Limitações em mapas interativos	Uso de bibliotecas otimizadas (Folium, GeoPandas)
Integração de múltiplas fontes	Implementação de um pipeline ETL padronizado
Problemas de desempenho	Modularização do código e uso de amostragem controlada
7. Considerações Éticas
Os dados utilizados serão públicos e anonimizados, respeitando normas de privacidade.
O modelo evitará viéses regionais, garantindo recomendações equilibradas para todas as províncias.
O projeto visa beneficiar comunidades locais, promovendo práticas de turismo justo e sustentável.



8. Resultados Esperados
Sistema funcional de recomendação turística inteligente adaptado à realidade angolana;
Mapas interativos e dashboards com indicadores de sustentabilidade e fluxo turístico;
Relatório técnico e científico descrevendo o processo de Machine Learning e impacto social do projeto;
Contribuição prática para políticas públicas e divulgação de destinos emergentes.
9. Repositório no GitHub
O projeto será versionado e documentado em:
📁 GitHub Repository: [github.com/<teu-usuario>/SmartTour-Angola](https://github.com/chissevo/NongoTour-Angola)
O repositório conterá:
/data → datasets originais e tratados
/notebooks → análises e modelagem ML
/src → código-fonte da aplicação
/docs → nota conceitual, plano e relatórios
README.md → descrição geral do projeto