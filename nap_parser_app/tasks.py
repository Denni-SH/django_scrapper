from __future__ import absolute_import, unicode_literals
from celery import shared_task
from nap_parser_app import models

@shared_task()
def add_product(product):
    models.Product.objects.get_or_create(
        id = product['id'],
        site = product['site'],
        url = product['url'],
        site_product_id = product['site_product_id'],
        name = product['name'],
        description = product['description'],
        brand = product['brand'],
        categories = ','.join(product['categories']),
        material = product['material'],
        images = ','.join(product['images'])
        )

@shared_task()
def add_price(price):
    models.Price.objects.get_or_create(
        id = price['id'],
        product_id = price['id'],
        site_product_id = price['site_product_id'],
        currency = price['currency'],
        date = price['date'],
        price = price['price'],
        stock_options = ','.join([str(item) for item in price['params']])
        )
