from django.db import models
from Accounts.models import Cust_register

# Create your models here

class Pets(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(max_length=100)
    breed=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)
    image=models.ImageField(upload_to='pets/')
    quantity=models.IntegerField(default=1)

class Cart(models.Model):
    user = models.ForeignKey(Cust_register,on_delete=models.CASCADE)
    pet = models.ForeignKey(Pets,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    grand_total = models.IntegerField(default=0)

class Payments(models.Model):
    user=models.ForeignKey(Cust_register,on_delete=models.CASCADE)
    pet=models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount=models.FloatField()
    payment_id=models.CharField()
    razorpay_payment_id=models.CharField()
    razorpay_order_id=models.CharField()
    razorpay_signature=models.CharField()

class Delivery_details(models.Model):
    user=models.ForeignKey(Cust_register,on_delete=models.CASCADE)
    pet=models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount=models.FloatField()
    user_token = models.FloatField()
    delivery_token=models.IntegerField()
    address=models.CharField()
    delivery_status=models.CharField(max_length=20, default='pending')
