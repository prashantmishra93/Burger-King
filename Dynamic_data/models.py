from django.db import models

# Create your models here.

class BurgerDetails:
    name:str
    img:str
    desc:str
    price:int
    specialoffer:bool

class ContactDetail:
    address:str
    call:int
    email:str
    img:str

class AboutImage:
    about:str

class Customer(models.Model):
    name= models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    specialoffer = models.BooleanField(default=False)

class MasterData(models.Model):
    chef = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pics')

class MenuCustomer(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    specialoffer = models.BooleanField(default=False)

class MenuCustomer2(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    specialoffer = models.BooleanField(default=False)

class MenuCustomer3(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    specialoffer = models.BooleanField(default=False)

class ContactData(models.Model):
    address = models.TextField(max_length=100)
    call = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=40)