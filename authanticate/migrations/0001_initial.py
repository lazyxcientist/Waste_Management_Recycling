# Generated by Django 3.2.2 on 2023-03-02 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.UUIDField(default=uuid.uuid4)),
                ('id_user', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('gender', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('user_status', models.CharField(default='user', max_length=100)),
                ('extra_data', models.TextField(default='{}')),
                ('reward_point', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
