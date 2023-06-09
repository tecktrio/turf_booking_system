# Generated by Django 4.0.8 on 2023-03-24 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_booked_turf_time_alter_users_manager_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked_turf',
            name='time',
            field=models.DateField(default=datetime.datetime(2023, 3, 24, 20, 35, 56, 298738)),
        ),
        migrations.AlterField(
            model_name='users',
            name='manager_status',
            field=models.CharField(choices=[('pending', 'pending'), ('True', 'True'), ('Talse', 'False')], default='False', max_length=20),
        ),
    ]
