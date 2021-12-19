# Generated by Django 4.0 on 2021-12-18 11:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_department_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.AlterField(
            model_name='department',
            name='client',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]
