from datetime import date
import calendar
curr_date = date.today()
def tt():
  daye = calendar.day_name[curr_date.weekday()]
  daye = daye.lower()
  def monday():
    x =  "wireless communication : 08:40 - 09:30\nRF systems             : 09:35 - 10:25 \nCPS                    : 10:30 - 11:20 \n DBMS                   : 12:20 - 01:10 \n"
    return x
  def tuesday():
    x = "CPS                    : 08:40 - 09:30 \nDBMS                   : 09:35 - 10:25 \nwireless communication : 10:30 - 11:20 \nRF systems             : 12:20 - 01:10 \nsoftware engineering   : 03:05 - 03:55 \n"
    return x
  def wednesday():
    x = "RF systems             : 08:40 - 09:30 \nwireless communication : 09:35 - 10:25 \nCPS                    : 11:25 - 12:15 \nsoftware engineering   : 12:20 - 01:10 \nEM/D&E LAB             : 02:10 - 04:50 \n"
    return x
  
  def thursday():
    x =  "EM/D&E LAB             : 08:40 - 11:20 \nCPS                    : 11:25 - 12:15 \nsoftware engineering   : 12:20 - 01:10 \ndisaster management    : 02:10 - 3:00 "
    return x
  def friday():
    x = "SSK                    : 08:40 - 11:20 \nwireless communication : 11:25 - 12:15 \nDBMS                   : 12:20 - 01:10" 
    return x
  if daye == 'monday':
    return monday()
  if daye == 'tuesday':
    return tuesday()
  if daye == 'wednesday':
    return wednesday()
  if daye == 'thursday':
    return thursday()
  if daye == 'friday':
    return friday()
  else:
    return "take some rest, enjoy your weekend!"
  
