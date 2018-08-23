# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiuproject.items import QiuprojectItem

class QiuniSpider(CrawlSpider):
    name = 'qiuni'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    page_link = LinkExtractor(allow=r'/8hr/page/\d+/')
    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )
    # 向第一页的url发送请求，从第一页的响应中提取的链接为  2345 13
    # 第二页的内容过来之后，还要提取链接    1345  13
    # 3   12456 13
    # 4   12356 13
    # 加入一共13页，每一页过来都要提取   1  12次 2 12次
    # 一共是13url    最终提取了100个url，调度器有去重的功能

    def parse_item(self, response):
        # 先得到所有的div
        div_list = response.xpath('//div[@id="content-left"]/div')
        for odiv in div_list:
            # 创建对象
            item = QiuprojectItem()
            # 得到头像
            face = odiv.xpath('./div[1]//img/@src').extract()[0]
            try:
                name = odiv.xpath('./div[1]/a/h2/text()')[0].extract().strip('\t\n \r')
            except Exception as identifier:
                name = '匿名用户'
            try:
                age = odiv.xpath('./div[1]/div/text()')[0].extract()
            except Exception as identifier:
                age = ''
            
            content = odiv.xpath('.//div[@class="content"]/span/text()').extract()
            content = ''.join(content).strip('\n\t ')

            # 好笑个数
            haha_count = odiv.xpath('./div[@class="stats"]/span[1]/i/text()')[0].extract()
            # 评论个数
            ping_count = odiv.xpath('./div[@class="stats"]/span[2]//i/text()')[0].extract()


            fields = ['face', 'name', 'age', 'content', 'haha_count', 'ping_count']
            for field in fields:
                item[field] = eval(field)
            
            # 将item扔给引擎
            yield item
