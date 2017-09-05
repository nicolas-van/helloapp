from django.core.management.base import BaseCommand, CommandError
from hello.models import *

class Command(BaseCommand):
    help = 'Prints hello'

    def add_arguments(self, parser):
        parser.add_argument('name_id', type=int)
    
    def handle(self, *args, **options):
        name = 'stranger'
        if 'name_id' in options:
            name = Name.objects.get(id = options['name_id']).name
            
        self.stdout.write("Hello %s" % name)
        
