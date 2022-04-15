import os
import telebot
import datetime
from weatherf import weather_data
from timetable import tt
from keep_alive import keep_alive
from help import help
x = str(datetime.datetime.now())

my_secret = os.getenv('API_KEY')
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands = ['hi'])
def hi(message):
  bot.reply_to(message,"hey, whassup!")

@bot.message_handler(commands = ['today'])
def today(message):
  bot.reply_to(message,x[:10])

@bot.message_handler(commands = ['weather'])
def weather(message):  
  bot.reply_to(message,weather_data())

@bot.message_handler(commands = ['tt'])
def tbt(message):  
  bot.reply_to(message,tt())
  
@bot.message_handler(commands = ['help'])
def hlp(message):  
  bot.reply_to(message,help())

 
keep_alive()
bot.polling()