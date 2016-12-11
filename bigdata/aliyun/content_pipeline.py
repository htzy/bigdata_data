# -*- coding: utf-8 -*-
import re
from scrapy.exceptions import DropItem


# clean content
class ContentPipeline(object):
    def process_item(self, item, spider):
        if re.search(u'window|线下|预告|报名地址', item['title'], re.I):
            print "ignore this item"
            raise DropItem("Contains word that you don't want: %s" % item['title'])
        elif re.search(u'window|线下|预告|报名地址', item['abstract'], re.I):
            print "ignore this item"
            raise DropItem("Contains word that you don't want: %s" % item['abstract'])
        else:
            return item
