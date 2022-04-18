import os
import requests


def weather_data(message):
  location = message
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
  '''
  print ("-------------------------------------------------------------")
  #print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
  print ("-------------------------------------------------------------")
  
  print ("Current temperature is: {:.2f} deg C".format(temp_city))
  print ("Current weather desc  :",weather_desc)
  print ("Current Humidity      :",hmdt, '%')
  print ("Current wind speed    :",wind_spd ,'kmph')
  '''
  tp = " current temperature in {} is {:.2f} degree celsius, is {} and humidity is {}%".format(location,temp_city,weather_desc,hmdt)

  return tp