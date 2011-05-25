
from django.utils import simplejson
from django.http import HttpResponse

def json_response(data=None):
  response = HttpResponse(mimetype="text/javascript; charset=utf8")
  if not data:
    data = { 'success': False }
  response.write(simplejson.dumps(data))
  return response

