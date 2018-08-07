# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    """
        爬虫的名字，启动爬虫的时候，要根据名字启动
        允许的域名，是一个列表，判断url在不在域名下面，如果在就发，不在就过滤
        start_urls  起始url列表,一般只写一个
        parse  回调函数，名字不要改,重写的函数，处理起始的url响应，response就是响应对象
               如果又返回值，要返回可迭代对象
    """
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com', 'www.baidu.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        # print('-'*80)
        # print(response)
        # <200 https://www.qiushibaike.com/>
        # print(type(response))
        # <class 'scrapy.http.response.html.HtmlResponse'>
        # print(response.text)
        # print('-'*80)

        #  先得到所有的div
        div_list = response.xpath('//div[@id="content-left"]/div')
        # print('*'*80)
        # print(div_list)
        # [<Selector xpath='//div[@id="content-left"]/div' data='<div class="article block
        #      untagged mb15 '>,...]
        # print(len(div_list))
        # print('*'*80)

        items = []
        for oDiv in div_list:
            try:
                face = oDiv.xpath('./div[1]/a/img/@src')[0].extract()
                name = oDiv.xpath('./div[1]/a/h2/text()')[0].extract().strip('\t\n\r')
                age = oDiv.xpath('./div[1]/div/text()')[0].extract()
                content = oDiv.xpath('./a[1]//span[1]/text()').extract()
                #  注意上面的content后面提取text()没有加[0]，为什么呢？
                #  如果加了就只能获取一行的数据
                #  因为<span>标签下面还包含了<br>标签
                #  所以我们获取到的是<span>标签下的所以内容，直接text()

                #  因为由\n换行符，所以我们需要重新拼接一下
                content = ''.join(content).strip('\n\t ')

                #  数据放到字典中
                item = {
                    '头像': face,
                    '网名': name,
                    'age': age,
                    '段子': content
                }
            except Exception as e:
                item = {}
            finally:
                items.append(item)
        return items
