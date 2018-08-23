# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from shetuproject.items import ShetuprojectItem

from scrapy_redis.spiders import RedisCrawlSpider

class PictureSpider(RedisCrawlSpider):
    name = 'pic'
    allowed_domains = ['699pic.com']
    
    redis_key = 'picturespider:start_urls'

    # 自己定义配置文件，优先使用这里配置的
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 400,
        },
        'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        'SCHEDULER_PERSIST': True,
        'REDIS_HOST': '10.0.118.25',
        'REDIS_PORT': 6379,
        'DOWNLOAD_DELAY': 1,
    }

    # 页码规则
    page_link = LinkExtractor(allow=r'/photo-0-13-\d+-0-0-0\.html')
    # 详情页规则
    detail_link = LinkExtractor(restrict_xpaths='//div[@class="list"]/a')
    # 第一页内容过来
    # 提取了好多页码的链接
    # 提取了第一页的详情页链接，第一页的图片就都处理了

    # 向2345 400发送请求之后，规则都没有走，所以没有下载，只下载了第一页

    rules = (
        Rule(page_link, follow=True),
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
