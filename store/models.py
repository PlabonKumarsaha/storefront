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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    birth_date =models.DateTimeField(null=True)
    