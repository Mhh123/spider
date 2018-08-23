# -*- coding: utf-8 -*-
import scrapy

from shetuproject.items import ShetuprojectItem


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/food.html']

    page = 1
    url = 'http://699pic.com/photo-0-13-{}-0-0-0.html'

    # 处理每一个图片详情链接的请求
    def parse_detail(self, response):
        # 创建一个对象，用来保存所有信息
        item = ShetuprojectItem()

        # 图片的名字
        item['name'] = response.xpath('//div[@class="photo-view"]/h1/text()')[0].extract()
        item['publish_time'] = response.xpath('//div[@class="photo-view"]/div[1]/span[1]/text()')[0].extract()
        item['look_count'] = response.xpath('//div[@class="photo-view"]/div[1]/span[2]/read/text()')[0].extract()
        item['collect'] = response.xpath('//div[@class="photo-view"]/div[1]/span[3]/text()')[0].extract().split(' ')[0]
        item['download'] = response.xpath('//div[@class="photo-view"]/div[1]/span[4]/text()')[1].extract().split(' ')[
            1].strip('\n\t')
        item['image_url'] = response.xpath('//div[@class="photo-img"]/a/@href')[0].extract()

        yield item

        # 如果想下载带防盗链的图片，在这里直接通过scrapy.Request发，就自动带reference；
        # yield scrapy.Request(url=item['image_url'], callback=self.download)

    # def download(self, response):
    #     with open('1.png', 'wb') as fp:
    #         fp.write(response.body)


    def parse(self, response):
        # 先找到所有的图片的详情链接
        href_list = response.xpath('//div[@class="list"]/a/@href').extract()
        # 向每一个详情来链接发送请求
        for href in href_list:
            yield scrapy.Request(url=href, callback=self.parse_detail)

        # 拼接url,接着发送第二页的请求
        if self.page <= 2:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)
