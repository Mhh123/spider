# -*- coding: utf-8 -*-
import scrapy

from qiubaiproject.items import QiubaiprojectItem


class QiuSpider(scrapy.Spider):
    name = 'qiu'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']


    # 实现爬取多页的代码
    page = 1
    url = 'https://www.qiushibaike.com/8hr/page/{}/'

    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        for oDiv in div_list:
            # 创建对象
            item = QiubaiprojectItem()
            face = oDiv.xpath('./div[1]//img/@src')[0].extract()
            try:
                name = oDiv.xpath('./div[1]//h2/text()')[0].extract().strip('\t\n\r')
            except Exception as identifier:
                name = '匿名用户'
            try:
                age = oDiv.xpath('./div[1]/div/text()')[0].extract()
            except Exception as identifier:
                age = ''
            content = oDiv.xpath('./a[1]//span[1]/text()').extract()

            content = ''.join(content).strip('\n\t ')

            # 好笑个数
            haha_count = oDiv.xpath('//div[@id="content-left"]/div/div[@class="stats"]/span[1]//i/text()')[0].extract()
            # 评论个数
            ping_count = oDiv.xpath('//div[@id="content-left"]/div/div[@class="stats"]/span[2]//i/text()')[0].extract()


            #  将内容全部保存到item
            item['face'] = face
            item['name'] = name
            item['age'] = age
            item['content'] = content
            item['haha_count'] = haha_count
            item['ping_count'] = ping_count


            #  将item扔给引擎,管道进行处理
            yield item
        # 接着爬取指定页面
        if self.page <= 5:
            self.page += 1
            url = self.url.format(self.page)
            # 相拼接好的url再次发送请求,扔给调度器进行处理
            yield scrapy.Request(url=url, callback=self.parse)

