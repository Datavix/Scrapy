# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    update_time = scrapy.Field()
    price = scrapy.Field()
    average_price = scrapy.Field()
    houseDesign_size_orientation_floor = scrapy.Field()
    propertyManagement_year = scrapy.Field()
    location_facilities = scrapy.Field()
    traffic = scrapy.Field()
    phone = scrapy.Field()
