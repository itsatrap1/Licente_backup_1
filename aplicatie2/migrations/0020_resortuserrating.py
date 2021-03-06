# Generated by Django 3.2.9 on 2022-05-10 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webscrapping', '0003_resorts_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicatie2', '0019_delete_resorts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResortUserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_rating', models.CharField(max_length=10)),
                ('rated_date', models.DateTimeField(auto_now_add=True)),
                ('resorts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webscrapping.resorts')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
