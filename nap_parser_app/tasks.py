from __future__ import absolute_import, unicode_literals
from celery import shared_task
from nap_parser_app import models

def add_product(products):
    for product in products:
        models.Product.objects.get_or_create(
            site = product['site'],
            url = product['url'],
            site_product_id = product['site_product_id'],
            name = product['name'],
            description = product['description'],
            brand = product['brand'],
            categories = ','.join(product['categories']),
            material = product['material'],
            images = ','.join(product['images']))

def add_price(prices):
    for price in prices:
        models.Price.objects.get_or_create(
            site_product_id = price['site_product_id'],
            currency = price['currency'],
            date = price['date'],
            price = price['price'],
            stock_options = ','.join(price['params']))

@shared_task()
def main_func(products, prices):
    add_product(products)
    add_price(prices)

