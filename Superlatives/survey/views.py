
from django.http import HttpResponse

def show_survey(request):
  return render_to_response('survey.html', {})

