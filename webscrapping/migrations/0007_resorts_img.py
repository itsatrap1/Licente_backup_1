# Generated by Django 3.2.9 on 2022-05-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapping', '0006_remove_resorts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='resorts',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
