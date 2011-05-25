
from django.contrib import admin
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
  name = models.CharField(max_length=100, unique=True)
  gender = models.CharField(max_length=1, choices=GENDER)
  year = models.CharField(max_length=1, choices=YEAR)
  staff = models.BooleanField(default=False)

class Question(models.Model):
  qtext = models.CharField(max_length=200, unique=True)

  def __unicode__(self):
    return self.qtext

class Answer(models.Model):
  question = models.ForeignKey(Question)
  resident = models.ForeignKey(Resident) # related_name = 'answer_set'

  def __unicode__(self):
    return self.question.qtext + ": " + self.resident.name

admin.site.register(Resident)
admin.site.register(Question)
admin.site.register(Answer)

