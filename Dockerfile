FROM python:3.13-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Evita que o Python escreva arquivos .pyc e garante que o output vá direto para o terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Copia APENAS o arquivo de dependências primeiro (Otimização de Cache)
COPY requirements.txt .

# 5. Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia o restante do código do projeto para dentro do container
COPY . .

# 7. Informa a porta que o container vai expor
EXPOSE 8000

# 8. Comando para iniciar a aplicação (ajustado para a porta 8000)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]