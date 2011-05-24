from django.db import models

# Create your models here.
GENDER = (
  ('m', 'Male'),
  ('f', 'Female'),
)

YEAR = (
  ('f', 'Frosh'),
  ('s', 'Sophomore'),
  ('j', 'Junior'),
  ('r', 'Senior'),
) 


class Resident(models.Model):
  name = models.CharField(max_length=200)
  gender = models.CharField(max_length=1, choices=GENDER)
  year = models.CharField(max_length=1, choices=YEAR)
  staff = models.BooleanField(default=False)

class Question(models.Model):
  qtext = models.CharField(max_length=200)

class Answer(models.Model):
  question = models.ForeignKey(Question)
  answer = models.ForiegnKey(Resident) # related_name = 'answer_set'

