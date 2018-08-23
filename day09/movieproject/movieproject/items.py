# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 第一个页面要的内容为
    post = scrapy.Field()
    name = scrapy.Field()
    _type = scrapy.Field()
    score = scrapy.Field()

    # 第二个页面要的内容为
    director = scrapy.Field()
    actor = scrapy.Field()
    editor = scrapy.Field()
    publish_time = scrapy.Field()
    info = scrapy.Field()
