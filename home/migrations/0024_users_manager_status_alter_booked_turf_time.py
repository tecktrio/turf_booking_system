# Generated by Django 4.0.8 on 2023-03-24 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_turf_user_email_alter_booked_turf_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='manager_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booked_turf',
            name='time',
            field=models.DateField(default=datetime.datetime(2023, 3, 24, 19, 37, 1, 209680)),
        ),
    ]