from scrapy import Request
from scrapy.spider import Spider
from bigdata.aliyun.items import SearchItem


# search web site
# https://yq.aliyun.com/search?type=ARTICLE&q=${keyword}
# only search article
# https://yq.aliyun.com/search/articles/?q={keyword}&idex=default&days=&p={pageNum}

class AliyunSpider(Spider):
    name = "aliyun"
    allowed_domains = ["aliyun.com"]
    start_urls = [
        "https://yq.aliyun.com/search/articles/?q=docker&idex=default&days=&p=1"
        # , "https://yq.aliyun.com/search/articles/?q=maven&idex=default&days=&p=1"
        # , "https://yq.aliyun.com/search/articles/?q=scala&idex=default&days=&p=1"
        # , "https://yq.aliyun.com/search/articles/?q=hadoop&idex=default&days=&p=1"
        # , "https://yq.aliyun.com/search/articles/?q=spark&idex=default&days=&p=1"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="media-body _articles-item-body"]'):
            item = SearchItem()
            # xpath('string(.)') can get all text in selector and remove <span>
            item['title'] = sel.xpath('h2/div/a').xpath('string(.)').extract()[0]
            # item['abstract'] = sel.xpath('div[2]').xpath('string(.)').extract()[0].strip()
            item['abstract'] = \
                ''.join(sel.xpath('div[@class="_search-articles-content"]/text()'
                                  '|'
                                  'div[@class="_search-articles-content"]//span/text()').extract()).strip()
            # item['abstract'] = sel.xpath('div[2]/div[2]/a/preceding-sibling::node()').extract()
            item['author'] = sel.xpath('div[@class="infos"]/span/a/text()').extract()[0]
            item['author_link'] = sel.xpath('div[@class="infos"]/span/a/@href').extract()[0]
            item['tags'] = ",".join(sel.xpath('div[@class="_groups-tags"]//a/text()').extract())
            item['viewers'] = sel.xpath('div[@class="actions clearfix"]/span[1]/text()').extract()[0]
            item['like'] = sel.xpath('div[@class="actions clearfix"]/span[2]/text()').extract()[0]
            item['comments'] = sel.xpath('div[@class="actions clearfix"]/span[3]/text()').extract()[0]
            item['time'] = sel.xpath('h2/span/time/@datetime').extract()[0]
            item['link'] = sel.xpath('h2/div/a/@href').extract()[0]
            yield item

        # new_url_node = response.xpath('//a[@rel="next"]/@href').extract()
        # if new_url_node:
        #     new_url = "https://yq.aliyun.com" + new_url_node[0]
        #     print new_url
        #     yield Request(new_url, callback=self.parse)
