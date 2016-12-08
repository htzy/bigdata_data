from scrapy.spider import Spider
from bigdata.aliyun.items import SearchItem
from lxml import etree

# search web site
# https://yq.aliyun.com/search?type=ARTICLE&q=${keyword}


class AliyunSpider(Spider):
    name = "aliyun"
    allowed_domains = ["aliyun.com"]
    start_urls = [
        "https://yq.aliyun.com/search?type=ARTICLE&q=docker"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=maven"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=scala"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=hadoop"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=spark"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="media _articles-item"]'):
            item = SearchItem()
            # TODO remove <a> and <span>
            item['title'] = sel.xpath('div[2]/h2/div/a').extract()

            yield item
