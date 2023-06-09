# Generated by Django 4.0.8 on 2023-03-25 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_contact_alter_booked_turf_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf',
            name='booked_slot_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_10',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_11',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_12',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_13',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_6',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_7',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_8',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='turf',
            name='booked_slot_9',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booked_turf',
            name='time',
            field=models.DateField(default=datetime.datetime(2023, 3, 25, 14, 29, 40, 930749)),
        ),
    ]
