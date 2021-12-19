from random import choice
import factory
import phonenumbers

from django.core.management.base import BaseCommand
from company.models import User
from faker import Faker
from faker.providers.phone_number.en_US import Provider


class CustomPhoneProvider(Provider):
    def phone_number(self):
        while True:
            phone_number = self.numerify(self.random_element(self.formats))
            parsed_number = phonenumbers.parse(phone_number, 'US')
            if phonenumbers.is_valid_number(parsed_number):
                return phonenumbers.format_number(
                    parsed_number,
                    phonenumbers.PhoneNumberFormat.E164
                )


def generate_username(*args):
    return fake.profile(fields=['username'])['username']


fake = Faker()
fake.add_provider(CustomPhoneProvider)

TYPES = [
        ('0', 'первичный'),
        ('1', 'повторный'),
        ('2', 'внешний'),
        ('3', 'косвенный'),
    ]

SEX = [
    ('M', 'Мужской'),
    ('F', 'Женский'),
    ('U', 'Неизвестно'),
]


class ClientFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.LazyAttribute(generate_username)
    email = factory.Faker('email')
    phone = factory.LazyAttribute(lambda _: fake.phone_number())
    # additional_phone_numbers = ''
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    middle_name = factory.Faker('name')
    type = factory.LazyAttribute(lambda x: choice(TYPES)[0])
    sex = factory.LazyAttribute(lambda x: choice(SEX)[0])
    # timezone = ''
    # vk = ''
    # fb = ''
    # ok = ''
    # instagram = ''
    # telegram = ''
    # whats_app = ''
    # viber = ''


class Command(BaseCommand):
    help = 'specify the number of clients you want to create'

    def add_arguments(self, parser):
        parser.add_argument('number')

    def handle(self, *args, **options):
        #  created rows
        for _ in range(0, int(options['number'])):
            user = ClientFactory()
            user.save()

        self.stdout.write(f"generated {options['number']} clients")
