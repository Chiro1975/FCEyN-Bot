#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os.path
import sys

import telegram
from base import *
from baseData import *
from telegram.ext import (
     Updater,
     CommandHandler
)
from telegram import (
        InlineKeyboardButton,
        InlineKeyboardMarkup,
        ChatAction,
        ParseMode
)

# Seccion de constantes:
# Idea para TOKEN: Que el bot lea un archivo de texto, en vez de hardcodearlo.
TOKEN = ''

#TOKEN  = '672449039:AAGYmzWUTU33DtvawyFyekhY9U1yMV4ZcRo'

# Estaria bueno poner estos mensajes en un archivo aparte
WELCOME_MESSAGE = "¡Hola! Escribi /help si no sabes los comandos"
DIFUSION_MESSAGE = ("Grupo para tareas de difusión de charlas de matematica: " +
                    "https://t.me/joinchat/DLkiixM8QHt53Al_5ZYDjA" +
                    "\n" +
                    "Canal de Youtube con contenido de charlas y coloquios:" +
                    "https://www.youtube.com/channel/" +
                    "UCaP4UdjleezecVaXBa7spkw/videos?app=desktop")
HELP_MESSAGE = ("/aplicada Correlativas en la orientación aplicada \n" +
                "/comedor Muestra el menu del mes \n" +
                "/difusion Grupo de difusión \n" +
                "/help Muestra este bonito mensaje \n" +
                "/online Dice si el Bot esta vivo \n" +
                "/listar Muestra los grupos de materias \n" +
                "/listaroptativas Muestra los grupos de materias optativas \n" +
                "/listarotros Muestra otros grupos \n" +
                "/pura Correlativas en la orientación pura \n")
ONLINE_MESSAGE = "Estoy con vida"


def checkToken():
    fileExists = os.path.isfile('./token.txt')
    if (fileExists):
        tokenFile = open('./token.txt', 'r')
        TOKEN = tokenFile.read().strip()
        return TOKEN
    else:
        tokenFile = open('./token.txt', 'w+')
        print("No se ha detectado un token para el bot, inserte su token en el archivo token")
        sys.exit() 

TOKEN = checkToken()
print(TOKEN)


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

 


def sendMessage(update, context, text):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)

# Le hace un select a la base de datos del tipo listable_type para obtener el
# conjunto de campos para mostrar
def list_buttons(update, context, listable_type):
    with db_session:
        buttons = select(group for group in listable_type if group.validated)\
                  .order_by(lambda group: group.name)
        keyboard = []
        columns = 3
        for k in range(0, len(buttons), columns):
            row = [InlineKeyboardButton(
                text = button.name, url=button.url, callback_data=button.url)
                for button in buttons[k:k + columns]]
            keyboard.append(row)
        reply_markup = InlineKeyboardMarkup(keyboard)
        msg = update.message.reply_text(text="Grupos: ",
                                        disable_web_page_preview=True,
                                        reply_markup=reply_markup, quote=False)
        context.sent_messages.append(msg)

# Estaria bueno hacerlo mas bonito, con la base de datos
def handlerInit():
    start_handler = CommandHandler('start', start)
    difusion_handler = CommandHandler('difusion', difusion)
    help_handler = CommandHandler('help', help)
    online_handler = CommandHandler('online', online)
    francisco_handler = CommandHandler('bardearFrancisco', bardearFrancisco)
    listarFisica_handler = CommandHandler('listarfisica', listarfisica)
    listarmatematica_handler = CommandHandler('listarmatematica', listarmatematica)
    optativasMatematica_handler = CommandHandler('listaroptativasmatematica', optativasMatematica)
    #pura_handler = CommandHandler('pura', pura)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(difusion_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(online_handler)
    dispatcher.add_handler(francisco_handler)
    dispatcher.add_handler(listarFisica_handler)
    dispatcher.add_handler(listarmatematica_handler)
    dispatcher.add_handler(optativasMatematica_handler)
    #dispatcher.add_handler(pura_handler)


def start(update, context):
    sendMessage(update, context, WELCOME_MESSAGE)
                             
def difusion(update, context):
    sendMessage(update, context, DIFUSION_MESSAGE)
                             
def help(update, context):
    sendMessage(update, context, HELP_MESSAGE)
                        
def online(update, context):
    sendMessage(update, context, ONLINE_MESSAGE)
                          

def bardearFrancisco(update, context):
    francisco = ["recursante infinito", "tenes olor a CBC", "cantaste Victoria antes de tiempo", "deja de dividir por 0", "sos más bobo que una segunda capa de pintura", "sos más trivial que el anillo {0}", "Matusalen se va a recibir antes que vos", "mereces hacer toda la carrera con Guccione", "hasta un bot te putea, ni el te quiere"]
    franciscoSend = "Che @Fran2_16, "+ francisco[0]
    sendMessage(update, context, franciscoSend)

# NO ANDAN
"""

def enviar_imagen(chat_id, context, file_path):
    context.bot.send_photo(chat_id = chat_id, photo=open(file_path, 'rb'))


def pura(update, context):
    enviar_imagen(update, context, 'img/correlativas-pura.jpg')


"""




def listarfisica(update, context):
    list_buttons(update, context, ListableFisica)


def listarmatematica(update, context):
	list_buttons(update, context, ListableMatematica)	


def optativasMatematica(update, context):
	list_buttons(update, context, ListableMatematicaOptativa)

#TODO		
'''
def listarOtros(update, context):
	#DJANGO! el vaquero negro.
'''



# Funcion que se encarga de inicializar el patcher con todas las funciones
handlerInit()

# Inicializa la base de datos cargada en el directorio
init_db("FyCENBot.sqlite3")

# No usar, funciones para cargar la base de datos
# completarBaseFisica()
# completarBaseMatematica()
# completarOptativas()

# A hacer polling!
updater.start_polling()
