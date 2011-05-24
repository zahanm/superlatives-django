
from django.http import HttpResponse

from survey.models import Resident, Question, Answer

def show_survey(request):
  questions = Question.objects.all()
  return render_to_response('survey.html', {'questions': questions})

