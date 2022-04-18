from datetime import datetime
def tt(message):
  req = message.text
  req = req.lower()
  l = ['tt', 'timetable', 'today','time table']
  if req in l:
    daye = datetime.today().weekday()+1
  elif req == 'monday' or req =='mon':
    daye =0
  elif req == 'tuesday' or req =='tue':
    daye =1
  elif req == 'wednesday' or req =='wed':
    daye =2
  elif req == 'thursday' or req =='thur':
    daye =3
  elif req == 'friday' or req =='fri':
    daye =4
  else: daye=99

  
  def monday():
    x =  "MONDAY:\nwireless communication : 08:40 - 09:30\nRF systems             : 09:35 - 10:25 \nCPS                    : 10:30 - 11:20 \n DBMS                   : 12:20 - 01:10 \n"
    return x
  def tuesday():
    x = "TUESDAY:\nCPS                    : 08:40 - 09:30 \nDBMS                   : 09:35 - 10:25 \nwireless communication : 10:30 - 11:20 \nRF systems             : 12:20 - 01:10 \nsoftware engineering   : 03:05 - 03:55 \n"
    return x
  def wednesday():
    x = "WEDNESDAY:\nRF systems             : 08:40 - 09:30 \nwireless communication : 09:35 - 10:25 \nCPS                    : 11:25 - 12:15 \nsoftware engineering   : 12:20 - 01:10 \nEM/D&E LAB             : 02:10 - 04:50 \n"
    return x
  
  def thursday():
    x =  "THURSDAY:\nEM/D&E LAB             : 08:40 - 11:20 \nCPS                    : 11:25 - 12:15 \nsoftware engineering   : 12:20 - 01:10 \ndisaster management    : 02:10 - 3:00 "
    return x
  def friday():
    x = "FRIDAY:\nSSK                    : 08:40 - 11:20 \nwireless communication : 11:25 - 12:15 \nDBMS                   : 12:20 - 01:10" 
    return x



    
  if daye == 0:
    return monday()
  if daye == 1:
    return tuesday()
  if daye == 2:
    return wednesday()
  if daye == 3:
    return thursday()
  if daye == 4:
    return friday()
  else:
    return "take some rest, enjoy your weekend!"
  
