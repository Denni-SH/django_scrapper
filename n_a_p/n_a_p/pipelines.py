# -*- coding: utf-8 -*-

from n_a_p import items
from nap_parser_app import tasks


class NAPPipeline(object):

    def process_item(self, item, spider):
        if type(item) is items.ProductItem:
            tasks.add_product.apply([dict(item),])
            # tasks.add_product.delay([dict(item),])
        if type(item) is items.PriceItem:
            tasks.add_price.apply([dict(item),])
            # tasks.add_price.delay([dict(item),])
        return item
