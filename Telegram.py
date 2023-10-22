#####   NOME:                   Bot_Telegran.ps1
#####   VERSÃO:                 1.0
#####   DESCRIÇÃO:              Script para enviar mensagem em um grupo do telegram.
#####   DATA DA CRIAÇÃO:        22/10/2023
#####   DATA DA MODIFICAÇÃO:    Sem modificações
#####   ESCRITO POR:            David Portela


import logging
from telegram import Bot

# Configuração do token do seu bot
TOKEN = "TOKEN_DO_BOT"

# Configuração de registro para debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def send_telegram_message():
    # Criação do objeto do bot
    bot = Bot(token=TOKEN)

    # ID do chat onde você deseja enviar a mensagem
    chat_id = "ID_DO_TELEGRAM"

    # Mensagem que você deseja enviar
    message_text = "Olá, mundo!"

    # Envie a mensagem
    await bot.send_message(chat_id=chat_id, text=message_text)

# Caso o compilador seja assíncrono
if __name__ == '__main__':
    import asyncio
    asyncio.run(send_telegram_message())

