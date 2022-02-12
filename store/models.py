from operator import mod
from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=100)
    discount = models.FloatField()
    

class Collection(models.Model):
    title = models.CharField(max_length=255)
    # the plus sign means that a reverse relation won't be created!
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')

class Product(models.Model):
    sku = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.CASCADE)
    # all the availabe promotions
    promotions = models.ManyToManyField(Promotion)
    

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
    
class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_FAILED = 'F'
    
    PAYEMET_CHOICES = [
        (PAYMENT_PENDING,'pending'),
        (PAYMENT_COMPLETED,'completed'),
        (PAYMENT_FAILED,'failed')]
    
    payment_status = models.CharField(max_length=1,choices=PAYEMET_CHOICES,default=PAYMENT_PENDING)
    # order should not be deleted so it is used as protected
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class OderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateField(auto_now_add=True)   


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()




class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    # adding parent class for one to one
    # customer = models.OneToOneField(Customer, on_delete= models.CASCADE, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)




    
    