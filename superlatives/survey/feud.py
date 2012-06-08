
import itertools

from survey.models import Resident, Question, Answer
from survey.utils import json_response

def export_top_k(k=6):
  answer_list = []
  for q in Question.objects.all():
    result = top_k_for_question(q, k)
    if len(result.answers) > 0:
      answer_list.append( result )
  return answer_list

def top_k_for_question(question, k=6):
  answers = question.answer_set.order_by('resident', 'resident2')
  groups = []
  if not len(answers):
    return { 'question': question.qtext }
  for resident, group in itertools.groupby(answers, lambda a: a.resident):
    if question.istwoans:
      g = list(group)
      groups.append( (len(g), resident.name, g[0].resident2.name ) )
    else:
      groups.append( (iterlen(group), resident.name, None) )
  groups.sort(reverse=True)
  answers = map( lambda g: { 'one': g[1], 'two': g[2], 'number': g[0] }, groups[:k] )
  return { 'question': question.qtext, 'answers': answers }

def iterlen(it):
  return sum(1 for _ in it)
