# Generated by Django 3.2.5 on 2022-03-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeApp', '0005_alter_order_tquan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ballance',
            name='tquan',
        ),
        migrations.RemoveField(
            model_name='ballance',
            name='ttime',
        ),
        migrations.AddField(
            model_name='ballance',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
