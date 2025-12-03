# Dockerfile
FROM python:3.10-slim

# Variáveis de ambiente para evitar prompts
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Cria diretório da aplicação
WORKDIR /app

# Copia requirements
COPY requirements.txt /app/

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o restante do projeto
COPY . /app/
