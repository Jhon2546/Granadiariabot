import logging
import schedule
import time
from telegram import Bot

# Token do bot (nunca compartilhe publicamente)
BOT_TOKEN = "8150152871:AAEpBlzsWYjjdsuPep2HjaycHcTHcEy4m5U"
CANAL_ID = "@rendaonline"  # Nome do seu canal

# Mensagens automáticas
mensagens = [
    "🎯 Oportunidade de hoje: Jogo NFT pagando no cadastro! Confira: https://exemplo.com/jogo1",
    "💸 Airdrop gratuito disponível! Ganhe tokens agora: https://exemplo.com/airdrop1"
]

# Inicializa o bot
bot = Bot(token=BOT_TOKEN)

# Ativa os logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Função que envia as mensagens
def enviar_mensagem():
    for msg in mensagens:
        try:
            bot.send_message(chat_id=CANAL_ID, text=msg)
            print(f"Mensagem enviada: {msg}")
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

# Agendamento das mensagens (UTC)
schedule.every().day.at("11:00").do(enviar_mensagem)  # 8h BRT
schedule.every().day.at("17:00").do(enviar_mensagem)  # 14h BRT

print("Bot iniciado. Aguardando horários...")

while True:
    schedule.run_pending()
    time.sleep(60)
