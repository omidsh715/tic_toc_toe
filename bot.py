import telebot
from telebot import apihelper

apihelper.proxy = {"http":"http://138.197.223.184"}

bot = telebot.TeleBot(token="1638487677:AAGpT9eFEv90PE95NFDK3Wi4fQfNUi-eiac")
@bot.message_handler(commands=["start","help"])
def send_welcome(message):
    bot.reply_to(message,"hey sir")

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message,message)

bot.polling()