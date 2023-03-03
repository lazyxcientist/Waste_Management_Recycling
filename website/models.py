from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Service_small(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    Address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)

    user_name = models.CharField(max_length=100)
    user_phone = models.IntegerField()
    user_phone2 = models.IntegerField()


    starting_date = models.DateField( default=datetime.now())
    ending_date = models.DateField(default=datetime.now())




class Service_details(models.Model):

    user_id = models.CharField(max_length=100)
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    starting_date = models.DateField()
    ending_date = models.DateField()

    
    