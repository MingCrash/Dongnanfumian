# -*- coding: utf-8 -*-
import re
import json
import scrapy
import requests
from dongnanfumian import helper
from scrapy.conf import settings
from dongnanfumian.items import DongnanfumianItem
from scrapy import Request

#雪球网
class XueqiuComSpider(scrapy.Spider):
    name = 'xueqiu.com'

    keywords = settings.get('KEYWORDS')

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'Cookie': '_ga=GA1.2.1364359570.1552362226; device_id=f9fd2cf8f50eb9d9a10f8b8758838739; aliyungf_tc=AQAAANnkNwdZLggA1H4geTEWd3MSMXAO; xq_a_token=8309c28a83ae5d20f26b7fcc22debbcd459794bd; xq_a_token.sig=ekfY9a_we8nNlhOpvhWeZz85MrU; xq_r_token=d55d09822791a788916028e59055668bed1b7018; xq_r_token.sig=h9qWLLwRXV-QxfHHukEC2U76ZDA; _gid=GA1.2.62523271.1552470820; u=981552470820277; Hm_lvt_1db88642e346389874251b5a1eded6e3=1552362227,1552470821; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1552470856',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    entry_point = 'https://xueqiu.com/statuses/search.json?sort=relevance&source=all&q={kw}&count=10&page={offset}'

    def start_requests(self):
        for i in self.keywords.keys():
            for j in range(self.keywords[i]):
                res = requests.get(url=self.entry_point.format(kw=i, offset=j),headers=self.headers)
                body = json.loads(res.text)
                for i in body['list']:
                    id = i['id']
                    title = i['title']
                    date = i['timeBefore']
                    author = i['user']['screen_name']
                    suburl = 'https://xueqiu.com'+i['target']
                    yield Request(url=suburl, callback=self.content_parse, headers=self.headers,
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
        pipleitem['S7'] = "PC"
        pipleitem['S2'] = '雪球网'
        pipleitem['Q1'] = response.xpath('string(//div[@class="article__bd__detail"])').extract_first()
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
