import pytz

from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey
from jsonfield import JSONField
from phonenumber_field.modelfields import PhoneNumberField


#  Client
class User(AbstractUser):
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

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.AutoField(primary_key=True)
    username = models.CharField('Логин', max_length=256, unique=True)
    email = models.EmailField('Почта')
    phone = PhoneNumberField('Номер Телефона', unique=True)
    additional_phone_numbers = JSONField('Дополнительные Номера', blank=True)
    last_name = models.CharField('Фамилия', max_length=36)
    first_name = models.CharField('Имя', max_length=36)
    middle_name = models.CharField('Отчество', max_length=36, blank=True)
    type = models.CharField('Тип', max_length=1, choices=TYPES, default=TYPES[0])
    sex = models.CharField('Пол', max_length=1, choices=SEX, default=SEX[0])
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    vk = JSONField('Вконтакте', blank=True)
    fb = JSONField('Фейсбук', blank=True)
    ok = models.CharField('Одноклассники', blank=True, max_length=36)
    instagram = models.CharField('Инстаграмм', blank=True, max_length=36)
    telegram = models.CharField('Телеграм', blank=True, max_length=36)
    whats_app = models.CharField('Ватсап', blank=True, max_length=36)
    viber = models.CharField('Вайбер', blank=True, max_length=36)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True, blank=True, null=True)

    @property
    def user_id(self):
        return f"{self.id}_01"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.username


#  Juristic Person
class JuristicPerson(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField('Полное название', max_length=256)
    abbreviation = models.CharField('Аббревиатура', max_length=16)
    inn = models.CharField('ИНН', max_length=10)
    kpp = models.CharField('КПП', max_length=9)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True, blank=True, null=True)
    department = models.ForeignKey('Department', verbose_name='Департаменты', on_delete=models.CASCADE)

    @property
    def jurist_id(self):
        return f"{self.id}_02"

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return self.full_name


class Department(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=256)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    client = models.ManyToManyField('User', verbose_name='Клиенты')

    class MPTTMeta:
        order_insertion_by = ['id']

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = 'Департаменты'

    @property
    def department_id(self):
        return f"{self.id}_03"

    def __str__(self):
        return self.name
