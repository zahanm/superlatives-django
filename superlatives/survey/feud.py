
import itertools

from survey.models import Resident, Question, Answer
from survey.utils import json_response

def export_top_k(k=6):
  answer_set = []
  for q in Question.objects.all():
    answers = top_k_for_question(q, k)
    if len(answers) > 0:
      answer_set.append( { 'question': q.qtext, 'answers': answers } )
  return answer_set

def top_k_for_question(question, k):
  answers = question.answer_set.order_by('resident', 'resident2')
  groups = []
  if not len(answers):
    return []
  for resident, group in itertools.groupby(answers, lambda a: a.resident):
    if question.istwoans:
      g = list(group)
      groups.append( (len(g), resident.name, g[0].resident2.name) )
    else:
      groups.append( (iterlen(group), resident.name) )
  groups.sort(reverse=True)
  return map( lambda g: g[1:], groups[:k] )

def iterlen(it):
  return sum(1 for _ in it)
