from operator import mod
from tkinter.tix import Tree
from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    

class Customer(models.Model):
    MEMEBERSHIP_BRONZE = 'B'
    MEMEBERSHIP_SILVER = 'S'
    MEMEBRSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMEBERSHIP_BRONZE,'Bronze'),
        (MEMEBERSHIP_SILVER,'Silver'),
        (MEMEBRSHIP_GOLD,'Gold')]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    birth_date =models.DateTimeField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMEBERSHIP_BRONZE)
    
class Order:
    placed_at = models.DateTimeField(auto_now_add=True)
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_FAILED = 'F'
    
    PAYEMET_CHOICES = [
        (PAYMENT_PENDING,'pending'),
        (PAYMENT_COMPLETED,'completed'),
        (PAYMENT_FAILED,'failed')]
    
    payment_status = models.CharField(max_length=1,choices=PAYEMET_CHOICES,default=PAYMENT_PENDING)
    
    