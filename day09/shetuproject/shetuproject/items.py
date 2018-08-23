# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShetuprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    publish_time = scrapy.Field()
    look_count = scrapy.Field()
    collect = scrapy.Field()
    download = scrapy.Field()
    image_url = scrapy.Field()
