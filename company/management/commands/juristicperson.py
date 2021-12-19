from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'specify the number of juristic persons you want to create'

    def add_arguments(self, parser):
        parser.add_argument('number')

    def handle(self, *args, **options):
        #  generate data

        self.stdout.write(f"generated {options['number']} juristic persons")
