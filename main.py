import os
import telebot
import datetime
from weatherf import weather_data
from timetable import tt
from keep_alive import keep_alive
from help import help
from validate import *
x = str(datetime.datetime.now())

my_secret = os.getenv('API_KEY')
bot = telebot.TeleBot(my_secret)


@bot.message_handler(func = validate_w)
def hi(message):
  bot.reply_to(message,"hey, whassup!")

@bot.message_handler(commands = ['today'])
def today(message):
  bot.reply_to(message,x[:10])


  
@bot.message_handler(commands = ['help'])
def hlp(message):  
  bot.reply_to(message,help())

@bot.message_handler(func = validate)
def send_msg(message):
  location = message.text.split()[1]
  x = ' hi, '+message.chat.first_name +weather_data(location)
  bot.send_message(message.chat.id,x)  

@bot.message_handler(func = validate_tt)
def txt(message):  
  bot.reply_to(message,tt(message))


 
keep_alive()
bot.polling()