# Dockerfile (Na raiz do vosso projeto)

# Imagem base mais leve para Python
FROM python:3.11.3

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os requisitos e instalá-los PRIMEIRO (cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Criar o diretório para os modelos
RUN mkdir -p /app/models

# Copiar os ficheiros principais (a API e os modelos)
COPY src/app.py /app/
COPY models/ /app/models/

# Expor a porta que o Flask vai usar
EXPOSE 5000

# Comando para executar o servidor (Gunicorn é profissional, mas Flask simples é mais rápido)
CMD ["python", "app.py"] 

# Requisitos para o requirements.txt:
# flask
# pandas
# numpy
# scikit-learn
# scipy
# joblib