from django.db import models
from  django.contrib.auth.models import timezone


class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    site = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    site_product_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    brand = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    images = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Price(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    site_product_id = models.IntegerField(default=0)
    currency = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0)
    stock_options = models.TextField(max_length=2000, default='None')

    def __str__(self):
        return str(self.product)