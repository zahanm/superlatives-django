
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
  if request.method == "POST":
    answer = Answer(
    question = Question.objects.get(id=request.POST['qid']),
    resident = Resident.objects.get(name=request.POST['resident']) )
    answer.save()
    return json_response({ 'success': True })
  else:
    questions = Question.objects.all()
    return render_to_response('survey.html', {'questions': questions},
        context_instance=RequestContext(request))

def thanks(request):
  return HttpResponse("Thanks!", mimetype="text/plain")

