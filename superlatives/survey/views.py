
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required

from survey.models import Resident, Question, Answer
from survey.utils import json_response

from django.conf import settings

import feud

class RestoredQuestion:
  def __init__(self, id, qtext, istwoans, prevans='', prevans2=''):
    self.id = id
    self.qtext = qtext
    self.istwoans = istwoans
    self.prevans = prevans
    self.prevans2 = prevans2

  def __unicode__(self):
    return self.qtext

def surveyjs(request):
  residents = Resident.objects.all()
  return render_to_response('survey.js', {'residents': residents},
      context_instance=RequestContext(request), mimetype="text/javascript")

@login_required
def survey(request):
  user = Resident.objects.get(sunetid=request.user.username)
  if request.method == "POST":
    question = Question.objects.get(id=request.POST['qid'])
    resident = Resident.objects.get(name=request.POST['resident'])
    if question.istwoans:
      resident2 = Resident.objects.get(name=request.POST['resident2'])
    try:
      answer = Answer.objects.get(
          question = question,
          answerer = user)
    except Answer.DoesNotExist:
      answer = Answer(
          question = question,
          answerer = user)
    answer.resident = resident
    if question.istwoans:
      answer.resident2 = resident2
    answer.save()
    return json_response({ 'success': True })
  else:
    questions = Question.objects.all()
    answered_set = user.answered_set.all()
    restored_qs = []
    for question in questions:
      restored_qs.append(RestoredQuestion(question.id, question.qtext,
        question.istwoans))
      matching_ans_set = answered_set.filter(question__exact=question)
      if matching_ans_set:
        restored_qs[-1].prevans = matching_ans_set.get().resident
        if restored_qs[-1].istwoans:
          restored_qs[-1].prevans2 = matching_ans_set.get().resident2
    return render_to_response('survey.html', {'questions': restored_qs, 'feuddatetime': settings.FEUD_DATE_TIME},
        context_instance=RequestContext(request))

@login_required
def results(request):
  if request.user.username not in settings.STAFF_SUNETIDS:
    return redirect('/')
  return HttpResponse(str(feud.export_top_k(6)), mimetype="text/plain")

def thanks(request):
  return HttpResponse("Thanks!", mimetype="text/plain")

