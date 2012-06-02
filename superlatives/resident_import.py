
import csv
from survey.models import Resident

r = csv.reader(open('roster.csv', 'rb'))
for row in r:
  name = row[3] + " " + row[2]
  sunetid = row[4].split("@stanford.edu")[0]
  gender = row[1].lower()
  year = 'f'
  if row[8] == "":
    staff = False
  else:
    staff = True
  rez = Resident(name=name, gender=gender, year=year, staff=staff, sunetid=sunetid)
  rez.save()
  print "Just saved: " + row[3]

print "Done"

  
