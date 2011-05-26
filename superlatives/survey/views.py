
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from survey.models import Resident, Question, Answer
from survey.utils import json_response

def surveyjs(request):
  residents = Resident.objects.all()
  return render_to_response('survey.js', {'residents': residents},
      context_instance=RequestContext(request), mimetype="text/javascript")

def survey(request):
  user = Resident.objects.get(sunetid=request.META['REMOTE_USER'])
  if request.method == "POST":
    answer = Answer(
    question = Question.objects.get(id=request.POST['qid']),
    resident = Resident.objects.get(name=request.POST['resident']) )
    answerer = user
    answer.save()
    return json_response({ 'success': True })
  else:
    questions = Question.objects.all()
    answered = user.answered_set.all()
    return render_to_response('survey.html', {'questions': questions,
      'answered': answered}, context_instance=RequestContext(request))

def thanks(request):
  return HttpResponse("Thanks!", mimetype="text/plain")

