from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.urls import reverse


User = get_user_model()

# Create your models here.

class Profile(models.Model):
    ids = models.UUIDField( default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    user_status = models.CharField(max_length=100, default='user')
    extra_data = models.TextField(default='{}')
    reward_point = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username
