# Generated by Django 3.2.5 on 2022-03-03 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sbs',
            name='number',
        ),
    ]
