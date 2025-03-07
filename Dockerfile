# Usa uma imagem base do Python (versão recomendada)
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto
COPY . .

# Define o PYTHONPATH para incluir o diretório do projeto
ENV PYTHONPATH=/app

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]