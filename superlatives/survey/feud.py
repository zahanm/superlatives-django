
import itertools

from survey.models import Resident, Question, Answer
from survey.utils import json_response

def export_top_k(k):
  q = Question.objects.all()[0]
  answers = top_k_for_question(q, k)
  return answers

def top_k_for_question(question, k):
  answers = question.answer_set.order_by('resident', 'resident2')
  groups = []
  for resident, group in itertools.groupby(answers, lambda a: a.resident):
    if question.istwoans:
      groups.append( (len(group), resident.name, group[0].resident2.name) )
    else:
      groups.append( (len(group), resident.name) )
  groups.sort(reverse=True)
  return map( lambda g: g[1:], groups[:k] )
