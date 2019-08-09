import telebot
import os

token = os.getenv("937310989:AAF7dZoQNzJ7pGt8vf84golvej2__AgUjvE%")
bot = telebot.TeleBot(token)
bot = telebot.TeleBot("937310989:AAF7dZoQNzJ7pGt8vf84golvej2__AgUjvE")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.send_message(message.chat.id, message.text)
	#bot.reply_to(message, message.text)
bot.polling(none_stop = True, interval = 0)
