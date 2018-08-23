# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class QiuprojectPipeline(object):
        # 一个函数是构造方法
    def __init__(self):
        # 可以保证文件只打开一次
        self.fp = open('qiu.txt', 'w', encoding='utf8')

    # 回调处理item函数，每一个item过来都会调用这个函数
    def process_item(self, item, spider):
        # 将item保存到文件中
        # 先将item转化为字典
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item
    
    def close_spider(self, spider):
        self.fp.close()

import pymysql
from scrapy.utils.project import get_project_settings
# 将数据存储到mysql中
class QiumysqlPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        # 获取数据库的所有信息
        host = settings['HOST']
        port = settings['PORT']
        user = settings['USER']
        password = settings['PASSWORD']
        db = settings['DBNAME']
        charset = settings['CHARSET']
        # 链接数据库
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)

    # 回调处理item函数，每一个item过来都会调用这个函数
    def process_item(self, item, spider):
        # 将item保存到数据库中
        sql = 'insert into qiubai(face, name, age, content, haha_count, ping_count) values("%s","%s","%s","%s","%s","%s")' % (item['face'], item['name'], item['age'], item['content'], item['haha_count'], item['ping_count'])
        cursor = self.conn.cursor()

        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print('*' * 100)
            print(e)
            print('*' * 100)
            self.conn.rollback()
        return item
    
    def close_spider(self, spider):
        self.conn.close()