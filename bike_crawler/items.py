# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


class BikeCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    site_url = scrapy.Field()
    bike_name = scrapy.Field()
    price = scrapy.Field(input_processor = MapCompose(str.strip))
    pass
