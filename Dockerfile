# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /app

# Copie os requisitos e instale as dependências
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o restante do código da aplicação
COPY src /app

# Exponha as portas necessárias
EXPOSE 5000 5001 5002 8001 50051

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
