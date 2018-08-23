# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShetuprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片名字
    name = scrapy.Field()
    # 发布日期
    publish_time = scrapy.Field()
    # 浏览量
    look_count = scrapy.Field()
    # 收藏量
    collect = scrapy.Field()
    # 下载量
    download = scrapy.Field()
    # 图片的url
    image_url = scrapy.Field()
