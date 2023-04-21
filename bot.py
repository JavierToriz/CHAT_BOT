from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import os

token = "6139150002:AAFEkPevOjAf_Av8n1JpuXuLGKmAKfsvJMs"

def start(bot,update):
    try:
        user_data = update.message.from_user
        update.message.reply_text("Hola estoy listo")
        print(f"{user_data}")
    except Exception as e: 
        print(f"Error start: {e.args}")  

def help(bot,update):
    try: 
        update.message.reply_text(f"Este bot tiene los siguientes comandos...")  
    except Exception as e:
        print(f"Error help: {e.args}")

def echo(bot,update):
    try:
        text = update.message.text #10,5
        #num1 = text[0]
        #num2 = text[1]
        #suma = int(num1) + int(num2)

        update.message.reply_text(f"{text}")

    except Exception as e:
        print(f"Error echo: {e.args}")

def operaciones(bot,update):
    try:
        text == update.message.text.split("+")
        num1 = text[0]
        num2 = text[1]
        suma = int(num1) + int(num2)   
        update.message.reply_text(f"{suma}") 
        
    except Exception as e:
        print(f"Error echo: {e.args}")

def image(bot, update):
    try:
        print("Recibiendo imagen")
        user_data = update.message.from_user
        print(user_data)
        file = bot.getFile(update.message.photo[-1].file_id)
        filename = os.path.join('downloads/images/','imagen.jpg')
        file.download(filename)
        update.message.reply_text(f"Imagen recibida")
    except Exception as e:
        print(f"Error image: {e.args}")

def error(bot,update,error):
    try:
        print(f"Update: {update} genero el error {error}")
    except Exception as e:
        print(f"Error en error: {e.args}")

def main():
    try:
        print("javivisBot iniciando el token")
        updater = Updater(token)
        print(f"javivisBot iniciando dispacher")
        dp= updater.dispatcher
        
        print("javivisBot iniciando commandHandler")
        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CommandHandler("help",help))
        dp.add_handler(CommandHandler("operaciones",operaciones))
        dp.add_handler(MessageHandler(Filters.text,operaciones))
        dp.add_handler(MessageHandler(Filters.photo,image))
        dp.add_error_handler(error)

        updater.start_polling()

        print("javivis iniciando el bot")
        updater.idle()

    except Exception as e:
        print(f"Error main : {e.args}")    

if __name__ == "__main__":
    main()