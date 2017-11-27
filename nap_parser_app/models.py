from django.db import models
from  django.contrib.auth.models import timezone


class Product(models.Model):
    site = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    site_product_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    brand = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    images = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    site_product_id = models.IntegerField(default=0)
    currency = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    price = models.FloatField(default=0)
    stock_options = models.CharField(max_length=100)

    def __str__(self):
        return self.product