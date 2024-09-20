from django.db import models

# Create your models here.

class Products(models.Model):
    Product_name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    Product_price  = models.FloatField(null=False, blank=False)


class Product_Bill(models.Model):
    Name = models.CharField(max_length=200)
    Quantity = models.IntegerField(null=False, blank=False)
    Price = models.FloatField(null=False, blank=False)
    Total_price = models.FloatField(null=False)
