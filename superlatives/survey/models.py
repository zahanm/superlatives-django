
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
  sunetid = models.CharField(max_length=100, unique=True)

  def __unicode__(self):
    return self.name

class Question(models.Model):
  qtext = models.CharField(max_length=200, unique=True)
  istwoans = models.BooleanField(default=False)

  def __unicode__(self):
    return self.qtext

class Answer(models.Model):
  question = models.ForeignKey(Question)
  resident = models.ForeignKey(Resident)
  resident2 = models.ForeignKey(Resident, default=None, null=True, related_name="answer2_set")
  answerer = models.ForeignKey(Resident, related_name="answered_set")

  def __unicode__(self):
    return str(self.question) + ": " + str(self.resident)

admin.site.register(Resident)
admin.site.register(Question)
admin.site.register(Answer)

