import os
import telebot
import datetime
import requests


x = str(datetime.datetime.now())

my_secret = os.getenv('API_KEY')




def weather_data():
  location = 'coimbatore'
  user_api = os.environ['w_key']
  complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
  api_link = requests.get(complete_api_link)
  api_data = api_link.json()
  
  #create variables to store and display data
  temp_city = ((api_data['main']['temp']) - 273.15)
  weather_desc = api_data['weather'][0]['description']
  hmdt = api_data['main']['humidity']
  wind_spd = api_data['wind']['speed']
  #date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
  
  print ("-------------------------------------------------------------")
  #print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
  print ("-------------------------------------------------------------")
  
  print ("Current temperature is: {:.2f} deg C".format(temp_city))
  print ("Current weather desc  :",weather_desc)
  print ("Current Humidity      :",hmdt, '%')
  print ("Current wind speed    :",wind_spd ,'kmph')
  tp = "Current temperature is: {:.2f} deg C".format(temp_city)
  return tp


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


 

bot.polling()