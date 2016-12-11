# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class SearchItem(Item):
    title = Field()
    abstract = Field()
    author = Field()
    author_link = Field()
    tags = Field()
    viewers = Field()
    like = Field()
    comments = Field()
    time = Field()
    link = Field()
