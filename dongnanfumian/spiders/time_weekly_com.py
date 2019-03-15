# -*- coding: utf-8 -*-
import re
import json
import scrapy
from dongnanfumian import helper
from scrapy import Request
from dongnanfumian.items import DongnanfumianItem
from scrapy.conf import settings
from scrapy_redis_bloomfilter.queue import PriorityQueue

class TimeWeeklyComSpider(scrapy.Spider):
    name = 'time.weekly.com'
    allowed_domains = ['app.time-weekly.com']
    # start_urls = ['http://http://app.time-weekly.com/timefinance/news/search/net/']

    keywords = settings.get('KEYWORDS')

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    entry_point = 'http://app.time-weekly.com/timefinance/news/search/net?keyword={kw}&page={offset}&pageSize=40&muid=A000009114F247&actionSource=1'

    def start_requests(self):
        for i in self.keywords.keys():
            for j in range(self.keywords[i]):
                yield Request(url=self.entry_point.format(kw=i, offset=j), callback=self.parse, headers=self.headers,
                              dont_filter=True)

    def parse(self, response):
        body = json.loads(response.text)
        if body['result'] == None: return
        for i in body['result']['list']:
            if 'article_url' in i.keys():
                id = i['id']
                title = i['title']
                date = helper.get_makedtime('%Y-%m-%d', i['time'])
                author = i['source']
                yield Request(url=i['article_url'], callback=self.parse, headers=self.headers,
                              meta={'id': id, 'title': title, 'date': date, 'author': author})

    def content_parse(self, response):
        pipleitem = DongnanfumianItem()

        pipleitem['S6'] = response.meta['date']
        pipleitem['S0'] = response.meta['id']
        pipleitem['S1'] = response.url
        pipleitem['S4'] = response.meta['title']
        pipleitem['S3a'] = '文章'
        pipleitem['G1'] = response.meta['author']
        pipleitem['S3d'] = None
        pipleitem['S7'] = "APP"
        pipleitem['S2'] = '时代财经APP'
        pipleitem['Q1'] = re.findall('content:([\S\s]*?)groupId:', response.text)[0]
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
