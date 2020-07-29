#Idea: Meter todos los handlers acá

def sendMessage(update, context, text):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)
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
