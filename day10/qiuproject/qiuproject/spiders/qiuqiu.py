# -*- coding: utf-8 -*-
import scrapy
# 导入链接提取器
from scrapy.linkextractors import LinkExtractor
# CrawlSpider导入之，现在使用这个模板
# Rule：规则类，指定提取的链接响应如何处理
from scrapy.spiders import CrawlSpider, Rule


class QiuqiuSpider(CrawlSpider):
    name = 'qiuqiu'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    # 写一个链接提取器
    lk = LinkExtractor(allow=r'Items/')
    # 定制规则元组
    '''
        参数1：写一个链接提取器对象
        参数2：用来处理这些提取的链接的响应
        【注1】parse函数在crawlspider中有非常重要的作用，其作用就是提取链接，千万不能重写，重写了crawlspider失效
        【注2】写法和普通Spider的callback不一样
            普通spider：self.parse_detail
            crawlspider: 'parse_detail'
        参数3：是否跟进，根据链接提取器提取了链接之后，这些链接发送请求得到响应之后，在这些响应里面要不要接着按照这个规则提取链接，要的话就是True，不要的话就是False
        follow默认值：如果规则里面有callback，follow不写默认为False，如果规则里面没有callback，follow不写默认为True
        '''
    rules = (
        Rule(lk, callback='parse_xxx', follow=True),
    )

    def parse_xxx(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
