# Generated by Django 4.0.8 on 2023-03-22 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_booked_turf_time_alter_turf_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked_turf',
            name='email',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='booked_turf',
            name='time',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 14, 41, 9, 230720)),
        ),
    ]
