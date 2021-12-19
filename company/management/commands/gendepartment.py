from random import choice
import factory

from django.core.management.base import BaseCommand
from company.models import Department
from faker.providers.company.en_US import Provider
from faker import Faker


class DepartmentFactory(factory.Factory):
    class Meta:
        model = Department

    middle_name = factory.Faker('name')


class Command(BaseCommand):
    help = 'specify the number of departments you want to create'

    def add_arguments(self, parser):
        parser.add_argument('number')

    def handle(self, *args, **options):
        #  created rows
        for _ in range(0, int(options['number'])):
            user = DepartmentFactory()
            user.save()

        self.stdout.write(f"generated {options['number']} departments")
