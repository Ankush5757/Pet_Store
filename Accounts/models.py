from django.db import models

# Create your models here.

class Cust_register(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    pin_code = models.CharField(max_length=6)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Profile_Pic(models.Model):  
    user = models.ForeignKey(Cust_register, on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='profile_pics/')  
    