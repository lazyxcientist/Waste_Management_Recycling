# Generated by Django 3.2.2 on 2023-03-03 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20230303_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_small',
            name='ending_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 3, 13, 58, 41, 270522)),
        ),
        migrations.AlterField(
            model_name='service_small',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 3, 13, 58, 41, 270522)),
        ),
    ]