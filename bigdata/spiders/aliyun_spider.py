from scrapy import Request
from scrapy.spider import Spider
from bigdata.aliyun.items import SearchItem


# search web site
# https://yq.aliyun.com/search?type=ARTICLE&q=${keyword}
# https://yq.aliyun.com/search/articles/?q={keyword}&idex=default&days=&p={pageNum}

class AliyunSpider(Spider):
    name = "aliyun"
    allowed_domains = ["aliyun.com"]
    start_urls = [
        "https://yq.aliyun.com/search/articles/?q=docker&idex=default&days=&p=49"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=maven"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=scala"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=hadoop"
        # , "https://yq.aliyun.com/search?type=ARTICLE&q=spark"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="media-body _articles-item-body"]'):
            item = SearchItem()
            # xpath('string(.)') can get all text in selector and remove <span>
            item['title'] = sel.xpath('h2/div/a').xpath('string(.)').extract()
            # item['abstract'] = sel.xpath('div[2]').xpath('string(.)').extract()[0].strip()
            item['abstract'] = \
                ''.join(sel.xpath('div[@class="_search-articles-content"]/text()'
                                  '|'
                                  'div[@class="_search-articles-content"]//span/text()').extract()).strip()
            # item['abstract'] = sel.xpath('div[2]/div[2]/a/preceding-sibling::node()').extract()
            item['author'] = sel.xpath('div[@class="infos"]/span/a/text()').extract()
            item['author_link'] = sel.xpath('div[@class="infos"]/span/a/@href').extract()
            item['tags'] = sel.xpath('div[@class="_groups-tags"]//a/text()').extract()
            item['viewers'] = sel.xpath('div[@class="actions clearfix"]/span[1]/text()').extract()
            item['like'] = sel.xpath('div[@class="actions clearfix"]/span[2]/text()').extract()
            item['comments'] = sel.xpath('div[@class="actions clearfix"]/span[3]/text()').extract()
            item['time'] = sel.xpath('h2/span/time/@datetime').extract()
            item['link'] = sel.xpath('h2/div/a/@href').extract()
            yield item

        new_url_node = response.xpath('//a[@rel="next"]/@href').extract()
        if new_url_node:
            new_url = "https://yq.aliyun.com" + new_url_node[0]
            print new_url
            yield Request(new_url, callback=self.parse)
