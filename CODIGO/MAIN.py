from TOKEN import TOKEN
import telebot

# Inicializa o bot
bot = telebot.TeleBot(TOKEN)

# Handler para o comando "/start"
@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    response = ""
    if user:
        response += "@" + user.username + "\n"
        response += "SEU ID: {}\n".format(user.id)
        response += "SEU NOME: {}\n".format(user.first_name)
        if user.last_name:
            response += "SEU SOBRENOME: {}\n".format(user.last_name)
        if user.language_code:
            response += "LINGUAGEM: {}\n".format(user.language_code)
    bot.send_message(message.chat.id, response)

# Inicia o bot com polling
bot.polling()
