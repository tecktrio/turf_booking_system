# Generated by Django 4.0.8 on 2023-03-21 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_booked_turf_slot_booked_turf_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turf',
            name='place',
        ),
        migrations.AlterField(
            model_name='booked_turf',
            name='time',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 16, 23, 34, 691534)),
        ),
    ]
