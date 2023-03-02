from django.db import models

# Create your models here.
class Subscription(models.Model):

    title = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.IntegerField(default=0)
    regular_price = models.IntegerField(default=0)
    off_percentage = models.IntegerField(default=0)
    duration= models.ImageField(default=0)
    reward_point = models.IntegerField()

    def __str__(self):
        return self.title
    


class Reward_product(models.Model):

    title = models.CharField(max_length=100)
    discription = models.TextField(default=0)
    points_required = models.IntegerField(default=0)
    coupen_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reward_product')
    expiray_date = models.DateField()
    starting_date = models.DateField()


