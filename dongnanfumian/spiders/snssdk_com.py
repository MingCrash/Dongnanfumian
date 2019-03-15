# -*- coding: utf-8 -*-
import re
import json
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import Request
from scrapy.conf import settings

#懂车帝APP
class SnssdkComSpider(scrapy.Spider):
    name = 'snssdk.com'

    keywords = settings.get('KEYWORDS')

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    entry_point = 'https://is.snssdk.com/motor/search/api/2/wap/search_content/?from=news&keyword={kw}&iid=65338592844&device_id=59868348056&ac=wifi&channel=huawei&aid=36&app_name=automobile&version_code=438&ab_client=a1%252Cc2%252Ce2%252Cf1%252Cg2%252Cf7&abflag=3&device_type=DUA-AL00&device_brand=HONOR&language=zh&os_api=27&os_version=8.1.0&uuid=A000009114F247&openudid=81e754ddcf1f3217&manifest_version_code=438&resolution=720%2A1356&dpi=320&update_version_code=4385&_rticket=1551863263302&search_sug=1&forum=1&cur_tab=1&motor_source=global&search_mode=common&city_name=%25E5%25B9%25BF%25E5%25B7%259E&gps_city_name=%25E5%25B9%25BF%25E5%25B7%259E&fp=PrTrLWctczc7FlwILSU1F2USP2Z7&as=A1A54CB7AF28DE1&cp=5C7F781DFE211E1&count=10&format=json&offset={offset}&search_from=h5&req_type=native&extra_params=%257B%257D&price_range=-1'

    def start_requests(self):
        for i in self.keywords.keys():
            for j in range(self.keywords[i]):
                yield Request(url=self.entry_point.format(kw=i,offset=j), callback=self.parse, headers=self.headers, dont_filter=True)

    def parse(self, response):
        body = json.loads(response.text)
        for i in body['data']:
            if 'article_url' in i.keys():
                id = i['id']
                title = i['abstract']
                date = helper.get_makedtime('%Y-%m-%d',i['create_time'])
                author = i['source']
                yield Request(url=i['article_url'], callback=self.content_parse, headers=self.headers,
                              meta={'id':id,'title':title,'date':date,'author':author})

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
        pipleitem['S2'] = '懂车帝APP'
        pipleitem['Q1'] = None
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
