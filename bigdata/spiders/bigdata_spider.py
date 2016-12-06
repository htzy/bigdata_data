from scrapy.spider import Spider
# from scrapy.selector import Selector

# from bigdata.items import BigdataItem
from bigdata.items import BigdataItem

class BigDataSpider(Spider):
    name = "bigdata"
    allowed_domains = ["aliyun.com"]
    start_urls = [
        "https://yq.aliyun.com/"
    ]

    #
    # def parse(self, response):
    #     filename = response.url.spilt("/")[-1]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         title = sel.xpath('a/text()').extract()
    #         link = sel.xpath('a/@href').extract()
    #         desc = sel.xpath('text()').extract()
    #         print title, link, desc
    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = BigdataItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link']=sel.xpath('a/@href').extract()
            item['desc']=sel.xpath('text()').extract()
            yield item
