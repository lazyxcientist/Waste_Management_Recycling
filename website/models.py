from django.db import models

# Create your models here.

class Service_small(models.Model):

    user_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)

    Address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)

    user_name = models.CharField(max_length=100)
    user_phone = models.IntegerField()
    user_phone2 = models.IntegerField()


    




class Service_details(models.Model):

    user_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)

    starting_date = models.DateField()
    ending_date = models.DateField()

    
    