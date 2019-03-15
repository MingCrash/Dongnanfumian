# encoding:utf-8
# Author: zhuzhiming

import re
import json
import scrapy
from scrapy.conf import settings
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import FormRequest,Request

#老司机APP
class EeoComCnSpider(scrapy.Spider):
    name = 'laosiji.com'

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    keywords = settings.get('KEYWORDS')

    payload = {
        'method': '/search/ywf/indexapi',
        'cityid': '257',
        'search': '思域',
        'type': '1',
        'page': '1'
    }

    def start_requests(self):
        for i in self.keywords.keys():
            for j in range(self.keywords[i]):
                self.payload['search'] = i
                self.payload['page'] = str(j)
                url = 'https://www.laosiji.com/proxy/api'
                yield FormRequest(url=url, callback=self.parse, formdata=self.payload, headers=self.headers, dont_filter=True)

    def parse(self, response):
        body = json.loads(response.text)
        if body['message'] != 'Success' : return
        for i in body['body']['search']['sns']['list']:
            date = i['publishtime']
            title = i['title']
            id = i['resourceid']
            author = i['user']['name']
            suburl = 'https://www.laosiji.com/thread/{}.html'.format(id)
            yield Request(url=suburl, callback=self.content_parse, headers=self.headers,
                      meta={'date':date,'title':title,'id':id,'author':author})

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
        pipleitem['S2'] = '老司机'
        content = response.xpath('string(//div[@class="threa-main-box"])').extract_first()
        if len(content) != 0:content = content.replace('\t','')
        pipleitem['Q1'] = content
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
