# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request


class ShetuprojectPipeline(object):

    def __init__(self):
        self.fp = open('image.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        obj = dict(item)
        string = json.dumps(obj)
        self.fp.write(string + '\n')

        # 下载图片函数
        self.download(item)
        return item

    def download(self, item):
        dirname = r'F:\untitled\scrapy_spider\day09\shetuproject\shetuproject\images'
        filename = item['name'] + '.' + item['image_url'].split('.')[-1]
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(item['image_url'], filepath)

    def close_spider(self, spider):
        self.fp.close()
