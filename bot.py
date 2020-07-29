#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Libraries
import os.path
import sys
import requests
from io import BytesIO

#Files
from base import *

#Toml
import toml
#Telegram
import telegram
#from baseData import *
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

# Estaria bueno poner estos mensajes en un archivo aparte
'''
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
<<<<<<< HEAD
'''
# Se carga el toml como un diccionario:
DATA_DICT = toml.load("datos.toml")
WELCOME_MESSAGE = DATA_DICT["MESSAGES"] ["WELCOME"]
DIFUSION_MESSAGE = DATA_DICT["MESSAGES"]["DIFUSION"]
HELP_MESSAGE = DATA_DICT["MESSAGES"]["HELP"]
ONLINE_MESSAGE = DATA_DICT["MESSAGES"]["ONLINE"]
TOKEN_FILE_PATH = './token.txt'
IMG = 'img/'
PATH_CORRELATIVA_PURA = IMG + 'correlativas-pura.jpg'
PATH_CORRELATIVA_APLICADA = IMG + 'correlativas-aplicada.jpg'

#Comprueba si existe el archivo del TOKEN, en caso que no, lo crea y avisa.
'''
def checkToken():
    fileExists = os.path.isfile(TOKEN_FILE_PATH)
    if (fileExists):
        tokenFile = open(TOKEN_FILE_PATH, 'r')
        TOKEN = tokenFile.read().strip()
        return TOKEN
    else:
        tokenFile = open(TOKEN_FILE_PATH, 'w+')
        print("No se ha detectado un token para el bot, inserte su token en el archivo token")
        sys.exit() 
'''

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

def enviar_imagen(chat_id, context, file_path):
    context.bot.sendChatAction(chat_id=chat_id, action=ChatAction.UPLOAD_PHOTO)
    msg = context.bot.send_photo(chat_id=chat_id, photo=open(file_path, 'rb'), quote=False)
    context.sent_messages.append(msg)        

# Estaria bueno hacerlo mas bonito, con la base de datos
def handlerInit():
   
    help_handler = CommandHandler('help', help)
    pura_handler = CommandHandler('pura', pura)
    start_handler = CommandHandler('start', start)
    online_handler = CommandHandler('online', online)
    difusion_handler = CommandHandler('difusion', difusion)
    aplicada_handler = CommandHandler('aplicada', aplicada)
    francisco_handler = CommandHandler('bardearFrancisco', bardearFrancisco)
    listarFisica_handler = CommandHandler('listarfisica', listarfisica)
    listarmatematica_handler = CommandHandler('listarmatematica', listarmatematica)
    optativasMatematica_handler = CommandHandler('listaroptativasmatematica', optativasMatematica)
    dispatcher.add_handler(pura_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(online_handler)
    dispatcher.add_handler(difusion_handler)
    dispatcher.add_handler(aplicada_handler)
    dispatcher.add_handler(francisco_handler)
    dispatcher.add_handler(listarFisica_handler)
    dispatcher.add_handler(listarmatematica_handler)
    dispatcher.add_handler(optativasMatematica_handler)

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
  

def pura(update, context):
    enviar_imagen(update.message.chat_id, context, PATH_CORRELATIVA_PURA)

def aplicada(update, context):
    enviar_imagen(update.message.chat_id, context, PATH_CORRELATIVA_APLICADA)    


def listarfisica(update, context):
    list_buttons(update, context, ListableFisica)


def listarmatematica(update, context):
	list_buttons(update, context, ListableMatematica)	


def optativasMatematica(update, context):
	list_buttons(update, context, ListableMatematicaOptativa)

#TODO		
'''
def listarOtros(update, context):
	#DJANGO! el vaquero negro del conourbano.
'''


global TOKEN
TOKEN = DATA_DICT["BOT"]["TOKEN"].strip()
#Funcion para comprobar que el TOKEN este bien inicializado 
#TOKEN = checkToken()

#Conecta el bot con Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

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
