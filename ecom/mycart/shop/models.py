from django.db import models
from django.contrib.postgres.fields import ArrayField

class Test(models.Model):
    test_name = models.CharField(max_length=50, default="")
    test_image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.test_name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length = 50,default="")
    prod_brand = models.CharField(max_length = 50,default="")
    prod_price = models.FloatField(default=0.0)
    prod_quantity = models.IntegerField(default=0)
    prod_desc = models.CharField(max_length = 3000, default="")
    prod_image = models.ImageField(upload_to='shop/images')
    prod_test = models.ForeignKey(Test,default=1,on_delete=models.SET_DEFAULT)
    
    def __str__(self):
        return self.prod_name

class Contact(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)
    c_email = models.CharField(max_length=70, default="")
    c_phone = models.CharField(max_length=70, default="")
    c_desc = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.c_name+'\'s'+" query"

class Order(models.Model):
    order_id = models.AutoField(primary_key= True)
    items_json = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    pin_code = models.CharField(max_length=6)


# Create your models here.
