
import itertools

from survey.models import Resident, Question, Answer
from survey.utils import json_response

def export_top_k(k=6):
  answer_list = []
  for q in Question.objects.all():
    result = top_k_for_question(q, k)
    if len(result['answers']) > 0:
      answer_list.append( result )
  return answer_list

def top_k_for_question(question, k=6):
  answers = question.answer_set.order_by('resident', 'resident2')
  groups = []
  if not len(answers):
    return { 'question': question.qtext, 'answers': [] }
  for resident, group in itertools.groupby(answers, grouping):
    if question.istwoans:
      groups.append( (iterlen(group), resident[0], resident[1] ) )
    else:
      groups.append( (iterlen(group), resident, None) )
  groups.sort(reverse=True)
  answers = map( lambda g: { 'one': g[1], 'two': g[2], 'number': g[0] }, groups[:k] )
  return { 'question': question.qtext, 'answers': answers }

def grouping(answer):
  if answer.resident2:
    r1 = answer.resident.name
    r2 = answer.resident2.name
    if r1 < r2:
      return (r1, r2)
    else:
      return (r2, r1)
  return answer.resident.name

def iterlen(it):
  return sum(1 for _ in it)
