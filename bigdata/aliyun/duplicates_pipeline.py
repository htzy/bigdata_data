# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['link'] in self.ids_seen:
            raise DropItem("Duplicate item found:%s" % item)
        else:
            self.ids_seen.add(item['link'])
            return item
