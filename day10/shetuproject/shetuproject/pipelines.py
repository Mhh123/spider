# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request

class ShetuprojectPipeline(object):
    def __init__(self):
        self.fp = open('image.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        obj = dict(item)
        string = json.dumps(obj)
        self.fp.write(string + '\n')

        # 下载图片函数
        # self.download(item)
        return item
    
    def download(self, item):
        dirname = r'C:\Users\ZBLi\Desktop\1806\day09\shetuproject\shetuproject\spiders\images'
        filename = item['name'] + '.' + item['image_url'].split('.')[-1]
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(item['image_url'], filepath)
    
    def close_spider(self, spider):
        self.fp.close()


import pymongo
class ShetumongoPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
    def process_item(self, item, spider):
        # 选择数据库,数据库为image
        db = self.client.image
        # 选择集合,集合的名字为image_info
        collection = db.image_info

        # 执行插入操作
        d = dict(item)
        collection.insert(d)
        return item
    
    def close_spider(self, spider):
        self.client.close()