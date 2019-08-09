import pyowm
import telebot
import os

token = os.getenv("937310989:AAF7dZoQNzJ7pGt8vf84golvej2__AgUjvE%")
bot = telebot.TeleBot(token)
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru") 
bot = telebot.TeleBot("937310989:AAF7dZoQNzJ7pGt8vf84golvej2__AgUjvE")

@bot.message_handler(content_types=['text'])
def send_echo(message):
        observation = owm.weather_at_place(message.text) 
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]

        answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
        answer = answer + "Температура сейчас в районе " + str(temp) + "\n\n"
        
        if temp < 10: 
                answer += "Сейчас очень холодно, одевайся как танк!"
        elif temp < 20: 
                answer += 'Сейчас холодно оденься потеплее' 
        else: 
                answer += 'Сейчас тепло одевайся как королева'
        
        bot.send_message(message.chat.id, answer)
	#bot.reply_to(message, message.text)
bot.polling(none_stop = True, interval = 0)

