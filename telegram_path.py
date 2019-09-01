import telebot

TOKEN = "824568611:AAGfJgHsjmiS8bA352MYGGGi6c-S6YRDwmk"
bot = telebot.TeleBot(TOKEN)
CHAT_ID = 377412691


def send_msg(msg):
    bot.send_message(CHAT_ID, msg)


def fail(msg):
    bot.send_message(CHAT_ID, 'Что-то пошло не так' + str(msg))
