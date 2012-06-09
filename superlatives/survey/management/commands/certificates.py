
from pprint import PrettyPrinter

from django.core.management.base import BaseCommand, CommandError

from survey.models import Resident, Question, Answer
from survey import feud

class Command(BaseCommand):

  help = 'Generates certificates for each resident'

  def handle(self, *args, **options):
    award_map = {}
    for r in Resident.objects.all():
      award_map[ r.name ] = []
    for q in Question.objects.filter(istwoans=False):
      result = feud.top_k_for_question(q, 1)
      if len(result['answers']):
        award_map[ result['answers'][0]['one'] ].append( str(result['answers'][0]['number']) + ' - ' + q.qtext )
    pp = PrettyPrinter(indent=2)
    pp.pprint(award_map)

if __name__ == '__main__':
  associate_names()
