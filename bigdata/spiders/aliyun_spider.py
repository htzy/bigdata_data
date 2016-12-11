from scrapy.spider import Spider
from bigdata.aliyun.items import SearchItem

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
            # xpath('string(.)') can get all text in selector and remove <span>
            item['title'] = sel.xpath('div[2]/h2/div/a').xpath('string(.)').extract()
            # item['abstract'] = sel.xpath('div[2]/div[2]').xpath('string(.)').extract()[0].strip()
            item['abstract'] = ''.join(sel.xpath('div[2]/div[2]/text() | div[2]/div[2]//span/text()').extract()).strip()
            # item['abstract'] = sel.xpath('div[2]/div[2]/a/preceding-sibling::node()').extract()
            item['author'] = sel.xpath('div[2]/div/span/a/text()').extract()
            item['authorLink'] = sel.xpath('div[2]/div/span/a/@href').extract()
            item['tags'] = sel.xpath('div[2]/div[3]//a/text()').extract()
            item['viewers'] = sel.xpath('div[2]/div[4]/span[1]/text()').extract()
            item['like'] = sel.xpath('div[2]/div[4]/span[2]/text()').extract()
            item['comments'] = sel.xpath('div[2]/div[4]/span[3]/text()').extract()
            item['time'] = sel.xpath('div[2]/h2/span/time/@datetime').extract()
            item['link'] = sel.xpath('div[2]/h2/div/a/@href').extract()
            yield item
