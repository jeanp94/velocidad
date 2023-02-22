import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Aquí se establece la clave de API de OpenAI
openai.api_key = "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"

# Aquí se establece el token de acceso del bot de Telegram
bot_token = "5112727671:AAFuGeeOuniE2SY5Pw6zMP3jGl78bO6nA-A"

# Función para responder mensajes de texto
def chat(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Función para responder comandos
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! ¡Soy un bot de ChatGPT en Telegram! ¡Pregúntame lo que quieras!")

# Crear el objeto del bot y establecer el manejador de eventos
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Establecer el manejador de comandos
dispatcher.add_handler(CommandHandler("start", start))

# Establecer el manejador de mensajes
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

# Iniciar el bot
updater.start_polling()
updater.idle()
