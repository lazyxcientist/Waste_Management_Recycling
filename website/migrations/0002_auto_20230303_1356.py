# Generated by Django 3.2.2 on 2023-03-03 08:26

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_details',
            name='id',
        ),
        migrations.RemoveField(
            model_name='service_small',
            name='id',
        ),
        migrations.AddField(
            model_name='service_small',
            name='ending_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 3, 13, 56, 13, 875664)),
        ),
        migrations.AddField(
            model_name='service_small',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 3, 13, 56, 13, 875664)),
        ),
        migrations.AlterField(
            model_name='service_details',
            name='service_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='service_small',
            name='service_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
