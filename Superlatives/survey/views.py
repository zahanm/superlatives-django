
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from survey.models import Resident, Question, Answer

def show_survey(request):
  questions = Question.objects.all()
  return render_to_response('survey.html', {'questions': questions},
      context_instance=RequestContext(request))

def surveyjs(request):
  residents = Resident.objects.all()
  return render_to_response('survey.js', {'residents': residents},
      context_instance=RequestContext(request), mimetype="text/javascript")

