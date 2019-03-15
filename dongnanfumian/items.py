# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongnanfumianItem(scrapy.Item):

    S0 = scrapy.Field()  # S0 id
    S1 = scrapy.Field()  # S1 url
    S2 = scrapy.Field()  # S2 webname
    S3a = scrapy.Field()  # S3a type
    S3d = scrapy.Field()  # S3d natvigate
    Q1 = scrapy.Field()  # Q1 content
    S4 = scrapy.Field()  # S4 title
    S5 = scrapy.Field()  # S5 crawl_time
    S6 = scrapy.Field()  # S6  date
    S7 = scrapy.Field()  # S7 platform
    G1 = scrapy.Field()  # G1 author