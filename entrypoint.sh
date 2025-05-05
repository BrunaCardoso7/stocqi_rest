#!/bin/bash

set -e

# Tenta conectar ao banco de dados no Render usando a URL de conexão
echo "Tentando conectar ao banco de dados PostgreSQL no Render..."
python << END
import sys
import psycopg2
import os
import time
import urllib.parse

max_attempts = 5
attempt = 0

# Obtém a URL de conexão das variáveis de ambiente
database_url = os.environ.get("DATABASE_URL")

if not database_url:
    print("Variável DATABASE_URL não encontrada!")
    sys.exit(1)

# Parse da URL de conexão
parsed_url = urllib.parse.urlparse(database_url)
dbname = parsed_url.path[1:]  # Remove o "/" inicial
user = parsed_url.username
password = parsed_url.password
host = parsed_url.hostname
port = parsed_url.port

while attempt < max_attempts:
    try:
        print(f"Tentativa {attempt + 1} de {max_attempts}...")
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
            sslmode='require'  # Para conexões seguras no Render
        )
        print("Conexão com o PostgreSQL estabelecida com sucesso!")
        conn.close()
        sys.exit(0)
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar: {e}")
        attempt += 1
        if attempt < max_attempts:
            print("Tentando novamente em 5 segundos...")
            time.sleep(5)
        else:
            print("Não foi possível conectar ao banco de dados após várias tentativas.")
            print("Continuando com a inicialização do aplicativo mesmo assim...")
END

# Mesmo que não consiga conectar, continua com a inicialização

# Collect static files if needed
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply migrations
echo "Applying migrations..."
python manage.py migrate --noinput

# Create superuser if environment variables are defined
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true
fi

# Execute the command passed to the container
exec "$@"