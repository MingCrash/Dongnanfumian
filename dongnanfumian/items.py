# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongnanfumianItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()       #S0
    url = scrapy.Field()      #S1
    webname = scrapy.Field()   #S2
    type = scrapy.Field()      #S3a
    natvigate = scrapy.Field()  #S3d
    content = scrapy.Field()    #Q1
    title = scrapy.Field()     #S4
    crawltime = scrapy.Field()   #S5
    date = scrapy.Field()     #S6
    platform = scrapy.Field()  #S7
    author = scrapy.Field()    #G1

