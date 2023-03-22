from django.db import models
import datetime
# Create your models here.  
class Turf(models.Model):
    turf_name = models.CharField(max_length=255,unique=True)
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    turf_image = models.ImageField(upload_to ='turf_images')
    description = models.CharField(max_length=255,default="")
    start = models.TimeField()
    end = models.TimeField()
    turf_size = models.CharField(max_length=40)
    contact = models.IntegerField(default=0)
    
    def __str__(self):
        return self.turf_name

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone_no = models.IntegerField()
    password = models.CharField(max_length=50)

class Booked_turf(models.Model):
    email = models.CharField(max_length=20,default='')
    turf_name = models.CharField(max_length=20)
    slot = models.CharField(max_length=20,default='none')
    time  = models.DateField(default=datetime.datetime.now())
    price  = models.IntegerField(default=0)
    location = models.CharField(max_length=100,default='')
    contact = models.IntegerField(default=0)
    

