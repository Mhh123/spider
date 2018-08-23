# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from shetuproject.items import ShetuprojectItem

class TupianSpider(CrawlSpider):
    name = 'tupian'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/food.html']

    # 页码规则
    page_link = LinkExtractor(allow=r'/photo-0-13-\d+-0-0-0\.html')
    # 详情页规则
    detail_link = LinkExtractor(restrict_xpaths='//div[@class="list"]/a')
    # 第一页内容过来
    # 提取了好多页码的链接
    # 提取了第一页的详情页链接，第一页的图片就都处理了

    # 向2345 400发送请求之后，规则都没有走，所以没有下载，只下载了第一页

    rules = (
        Rule(page_link, follow=False),
        Rule(detail_link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # 创建一个对象，用来保存所有的信息
        item = ShetuprojectItem()
        # 图片的名字
        item['name'] = response.xpath('//div[@class="photo-view"]/h1/text()').extract()[0]
        # 发布时间
        item['publish_time'] = response.xpath('//span[@class="publicityt"]/text()')[0].extract()
        # 浏览量
        item['look_count'] = response.xpath('//span[@class="look"]//read/text()').extract_first()
        # 收藏量
        item['collect'] = response.xpath('//span[@class="collect"]/text()')[0].extract().strip(' 收藏')
        # 下载量
        item['download'] = response.xpath('//span[@class="download"]/text()')[1].extract().strip(' 下载\n\t')
        # 图片的url
        item['image_url'] = response.xpath('//img[@id="photo"]/@src').extract_first()

        yield item
