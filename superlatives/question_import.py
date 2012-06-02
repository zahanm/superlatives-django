
FILE_NAME = "QUESTIONS"

from survey.models import Question

f = open(FILE_NAME)

for line in f:
  line = line.strip()
  q = Question(qtext=line)
  q.save()


  
