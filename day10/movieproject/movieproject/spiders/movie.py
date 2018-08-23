# -*- coding: utf-8 -*-
import scrapy
from movieproject.items import MovieprojectItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie']

    def parse(self, response):
        # 先找到所有的电影div列表
        div_list = response.xpath('xxx')
        for odiv in div_list:
            item = MovieprojectItem()
            # 获取电影海报
            item['post'] = response.xpath('xxx')
            # 获取电影类型
            item['_type'] = response.xpath('')
            # 获取电影名字
            item['name'] = response.xpath('')
            # 获取电影评分
            item['score'] = response.xpath('')

            # 获取电影的详情页链接
            detail_url = response.xpath('')
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

            # yield item
    def parse_detail(self, response):
        # 获取传递的参数
        item = response.meta['item']
        # 获取导演
        item['director'] = response.xpath()
        # 获取主演
        # 获取编剧
        # 获取发布时间
        # 获取电影简介

        yield item

