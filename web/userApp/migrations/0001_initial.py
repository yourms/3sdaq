# Generated by Django 3.2.5 on 2022-03-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SBS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(max_length=100)),
                ('title', models.TextField(max_length=100)),
                ('url', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(max_length=100)),
                ('user_pwd', models.TextField(max_length=100)),
                ('user_name', models.TextField(max_length=100)),
                ('user_point', models.IntegerField(default=1000)),
                ('user_regdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
