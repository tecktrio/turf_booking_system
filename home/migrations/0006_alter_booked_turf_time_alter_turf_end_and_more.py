# Generated by Django 4.0.8 on 2023-03-21 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_turf_place_alter_booked_turf_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked_turf',
            name='time',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 16, 25, 17, 123169)),
        ),
        migrations.AlterField(
            model_name='turf',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='turf',
            name='start',
            field=models.TimeField(),
        ),
    ]