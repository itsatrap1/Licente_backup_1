# Generated by Django 3.2.9 on 2022-04-05 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie2', '0012_resorts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resorts',
            name='user',
        ),
    ]
