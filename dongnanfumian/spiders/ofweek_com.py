# -*- coding: utf-8 -*-
import re
import json
import scrapy
from dongnanfumian import helper
from scrapy.conf import settings
from dongnanfumian.items import DongnanfumianItem
from scrapy import Request,FormRequest

class OfweekComSpider(scrapy.Spider):
    name = 'ofweek.com'

    keywords = settings.get('KEYWORDS')

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    data = {
        'news_type': '1',
        'keywords': '思域',
        'page': '1'
    }

    entry_point = 'https://mp.ofweek.com/search/ajax_search_news'

    def start_requests(self):
        for i in self.keywords.keys():
            for j in range(self.keywords[i]):
                self.data['keywords'] = i
                self.data['page'] = str(j)
                yield FormRequest(url=self.entry_point,formdata=self.data,callback=self.parse,headers=self.headers,dont_filter=True)

    def parse(self, response):
        body = json.loads(response.text)
        if len(body['data']) == 0:return
        for i in body['data']['list']:
            id = i['id']
            title = i['title']
            date = i['addtime']
            author = i['public_name']
            yield Request(url=i['url'], callback=self.content_parse, headers=self.headers,
                          meta={'id':id,'title':title,'date':date,'author':author})

    def content_parse(self, response):
        pipleitem = DongnanfumianItem()

        pipleitem['S6'] = response.meta['date']
        pipleitem['S0'] = response.meta['id']
        pipleitem['S1'] = response.url
        pipleitem['S4'] = response.meta['title']
        pipleitem['S3a'] = '文章'
        pipleitem['G1'] = response.meta['author']
        pipleitem['S3d'] = response.xpath('string(//div[@class="fl m-home_href"])').extract_first()
        pipleitem['S7'] = "PC"
        pipleitem['S2'] = '维科号'
        pipleitem['Q1'] = response.xpath('string(//div[@class="main"])').extract_first()
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
