from django.db import models
import datetime
# Create your models here.  
class Turf(models.Model):
    turf_name = models.CharField(max_length=255,unique=True)
    user_email = models.CharField(max_length=255,default='')
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    turf_image = models.ImageField(upload_to ='turf_images')
    description = models.CharField(max_length=255,default="")
    turf_size = models.CharField(max_length=40)
    contact = models.IntegerField(default=0)
    slot_9_10a = models.BooleanField(default=False)#from 9 am to 10 am
    slot_10_11 = models.BooleanField(default=False)# from 10 am to 11 am
    slot_11_12 = models.BooleanField(default=False)# from 11 am to 12 pm
    slot_12_1 = models.BooleanField(default=False)# from 12 pm to 1 pm
    slot_1_2 = models.BooleanField(default=False)#from 1pm to 2 pm
    slot_2_3 = models.BooleanField(default=False)#from 2pm to 3pm 
    slot_3_4= models.BooleanField(default=False)#from 3pm to 4pm
    slot_4_5 = models.BooleanField(default=False)#from 4pm to 5pm
    slot_5_6 = models.BooleanField(default=False)#from 5pm to 6pm 
    slot_6_7 = models.BooleanField(default=False)#from 6pm to 7pm 
    slot_7_8= models.BooleanField(default=False)# from 7pm to 8pm
    slot_8_9 = models.BooleanField(default=False)#from 8pm to 9pm
    slot_9_10 = models.BooleanField(default=False)#from 9pm to 10pm
    
    def __str__(self):
        return self.turf_name

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    manager_status = models.CharField(default='False',max_length=20,choices=(('pending','pending'),('True','True'),('Talse','False')))
    phone_no = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.email

class Booked_turf(models.Model):
    email = models.CharField(max_length=20,default='')
    turf_name = models.CharField(max_length=20)
    slot = models.CharField(max_length=20,default='none')
    time  = models.DateField(default=datetime.datetime.now())
    price  = models.IntegerField(default=0)
    location = models.CharField(max_length=100,default='')
    contact = models.IntegerField(default=0)
    
class Manager_Requests(models.Model):
    user = models.ForeignKey(Users,models.CASCADE)
    def __str__(self) -> str:
        return self.user.email

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    subject= models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.email