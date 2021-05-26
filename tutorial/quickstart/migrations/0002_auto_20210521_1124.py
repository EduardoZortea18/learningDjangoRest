# Generated by Django 3.2.3 on 2021-05-21 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date)),
                ('reminder', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='BookModel',
        ),
    ]