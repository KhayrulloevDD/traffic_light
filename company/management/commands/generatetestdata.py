import random
import factory
import phonenumbers

from django.core.management.base import BaseCommand
from company.models import User, Department, JuristicPerson
from faker import Faker
from faker.providers.phone_number.en_US import Provider


CLIENTS_COUNT = 30000
DEPARTMENTS_COUNT = 500
JURISTIC_PERSONS_COUNT = 200


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
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    middle_name = factory.Faker('name')
    type = factory.LazyAttribute(lambda x: random.choice(TYPES)[0])
    sex = factory.LazyAttribute(lambda x: random.choice(SEX)[0])
    # additional_phone_numbers = ''
    # timezone = ''
    # vk = ''
    # fb = ''
    ok = phone
    instagram = phone
    telegram = phone
    whats_app = phone
    viber = phone


def get_random_department():
    last = Department.objects.count() - 1
    index = random.randint(0, last)
    return Department.objects.all()[index]


def get_random_clients():
    last = User.objects.count() - 1
    counter = 0
    clients = []
    while counter < last:
        clients.append(User.objects.all()[counter])
        counter += random.randint(1, 10)
    return clients


class DepartmentFactory(factory.Factory):
    class Meta:
        model = Department

    name = factory.Faker('job')
    parent = get_random_department()  # factory.SubFactory('company.management.commands.generatetestdata.DepartmentFactory')
    # client = factory.SubFactory(ClientFactory)

    @factory.post_generation
    def client(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for elem in extracted:
                self.client.add(elem)


class JuristicPersonFactory(factory.Factory):
    class Meta:
        model = Department

    middle_name = factory.Faker('name')


class Command(BaseCommand):
    help = 'create dummy data for models client, department and juristic person'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('number')

    def handle(self, *args, **options):
        #  create Clients
        users = ClientFactory.create_batch(CLIENTS_COUNT)
        User.objects.bulk_create(users)

        #  create Departments
        # TODO
        # DepartmentFactory.create(client=get_random_clients())
        # Department.objects.bulk_create(departments)

        # #  create Juristic Persons
        # juristic_person = JuristicPersonFactory.create_batch(2)
        # JuristicPerson.objects.bulk_create(juristic_person)

        self.stdout.write(f"generated {CLIENTS_COUNT} clients, {DEPARTMENTS_COUNT} departments and "
                          f"{JURISTIC_PERSONS_COUNT} juristic persons")
