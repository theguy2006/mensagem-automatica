
import requests
import os

# Credenciais armazenadas no GitHub
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Endereço da API
url = f"https://api.telegram.org/bot{bosta}/sendMessage"

# Mensagem
dados = {
    "chat_id": CHAT_ID,
    "text": "Bom dia! Tenha um excelente dia! ☀️"
}

# Enviar mensagem
resposta = requests.post(url, json=dados)

# Verificar resultado
resposta.raise_for_status()

print("Mensagem enviada com sucesso!")
