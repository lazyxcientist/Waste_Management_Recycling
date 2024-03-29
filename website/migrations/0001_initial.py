# Generated by Django 3.2.2 on 2023-03-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('service_id', models.CharField(max_length=100)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service_small',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('service_id', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_no', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_phone', models.IntegerField()),
                ('user_phone2', models.IntegerField()),
            ],
        ),
    ]
