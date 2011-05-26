
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from survey.models import Resident, Question, Answer
from survey.utils import json_response

class RestoredQuestion:
  def __init__(self, id, qtext, prevans=None):
    self.id = id
    self.qtext = qtext
    self.prevans = prevans

  def __unicode__(self):
    return self.qtext

def surveyjs(request):
  residents = Resident.objects.all()
  return render_to_response('survey.js', {'residents': residents},
      context_instance=RequestContext(request), mimetype="text/javascript")

def survey(request):
  user = Resident.objects.get(sunetid=request.META['REMOTE_USER'])
  if request.method == "POST":
    answer = Answer(
      question = Question.objects.get(id=request.POST['qid']),
      resident = Resident.objects.get(name=request.POST['resident']),
      answerer = user)
    answer.save()
    return json_response({ 'success': True })
  else:
    questions = Question.objects.all()
    answered_set = user.answered_set.all()
    restored_qs = []
    for question in questions:
      restored_qs.append(RestoredQuestion(question.id, question.qtext))
      matching_ans_set = answered_set.filter(question__exact=question)
      if matching_ans_set:
        restored_qs[-1].prevans = matching_ans_set.get().resident
    return render_to_response('survey.html', {'questions': restored_qs},
        context_instance=RequestContext(request))

def thanks(request):
  return HttpResponse("Thanks!", mimetype="text/plain")

