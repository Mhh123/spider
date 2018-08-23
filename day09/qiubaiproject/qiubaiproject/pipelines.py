# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QiubaiprojectPipeline(object):
    # 一个函数是构造方法
    def __init__(self):
        # 可以保证文件只打开一次
        self.fp = open('qiu.txt', 'w', encoding='utf-8')

    # 爬虫文件启动的时候运行的函数
    # def open_spider(self,spider):
    # fp = open('qiu.txt', 'w', encoding='utf-8')
    # 回调处理item函数，每一个item过来都会调这个函数
    def process_item(self, item, spider):
        """  __init__和open_spider只要重写一个就行了"""
        # 将item保存到文件中
        # 先将item转化为字典
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item
    def close_spider(self, spider):
        self.fp.close()
