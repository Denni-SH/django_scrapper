# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import ProductItem, PriceItem
from nap_parser_app.tasks import main_func


class NAPPipeline(object):

    count = 0
    products = []
    prices = []

    def process_item(self, item, spider):
        if type(item) == ProductItem:
            self.products.append(dict(item))
            self.count += 1
        else:
            self.prices.append(dict(item))
            self.count += 1
        if self.count >= 1000:
            self.save_items()
            self.count = 0
        return item

    def save_items(self):
        main_func.delay(self.products, self.prices)
        self.products = []
        self.prices = []

    def close_spider(self, spider):
        main_func.delay(self.products, self.prices)