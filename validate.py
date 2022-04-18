
def validate(message):
  req = message.text.split()
  if len(req)<2:
    return False
  else:
    return True

def validate_tt(message):
  req = message.text
  req = req.lower()
  l = ['tt', 'timetable', 'today','time table','monday','tuesday','wednesday','thursday','friday','saturday','sunday','sun','mon','tue','thur','fri','sat']
  if req in l:
    return True
  else:
    return False

def validate_w(message):
  req = message.text
  req = req.lower
  l =['hi']
  if req in l:
    return True
  else:
    return False

  
  