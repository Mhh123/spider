# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from movieproject.items import MovieprojectItem


class MmSpider(CrawlSpider):
    name = 'mm'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie']

    # 如果修改为详情页提取所有的信息，那么就和摄图网是一摸一样的修改方式
    # 

    page_link = LinkExtractor(allow=r'/movie/?page=\d+')
    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
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
