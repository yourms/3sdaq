# Generated by Django 3.2.5 on 2022-03-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeApp', '0011_comp_u_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='D_trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('volume', models.IntegerField(default=0)),
                ('trade_cost', models.IntegerField(default=0)),
                ('ex_index', models.IntegerField(default=0)),
                ('regdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
