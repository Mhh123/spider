# -*- coding: utf-8 -*-
import scrapy
from shetuproject.items import ShetuprojectItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/food.html']

    page = 1
    url = 'http://699pic.com/photo-0-13-{}-0-0-0.html'

    def parse(self, response):
        # 首先得到所有的图片的详情链接
        href_list = response.xpath('//div[@class="list"]/a/@href').extract()
        # 向每一个详情链接发送请求
        for href in href_list:
            yield scrapy.Request(url=href, callback=self.parse_detail)
        
        # 拼接url，接着发送第二页的请求
        if self.page <= 2:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)
    
    # 处理每一个图片详情链接的请求
    def parse_detail(self, response):
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

    #     yield scrapy.Request(url=item['image_url'], callback=self.download)
    
    # def download(self, response):
    #     with open('1.png', 'wb') as fp:
    #         fp.write(response.body)

