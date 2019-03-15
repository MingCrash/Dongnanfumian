# -*- coding: utf-8 -*-
import re
import json,time
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy.conf import settings
from scrapy import Request

# 搜狐新闻app  {"code":91000,"msg":"empty data list"} 没数据
class EeoComCnSpider(scrapy.Spider):
    name = 'api.k.sohu.com'
    # allowed_domains = ['https://api.k.sohu.com/api/search/v5/search.go']

    keywords = settings.get('KEYWORDS')


    querystring = {"rt": "json", "pageNo": "2", "words": "思域", "p1": "NjUwOTMxNTExMjU1NjczNjUzOA%3D%3D",
                   "pageSize": "20", "type": "0", "gid": "x011060802ff0f509854f181600023703a473ca12949",
                   "apiVersion": "42", "sid": "10", "u": "1", "keyfrom": "input", "refertype": "1",
                   "versionName": "6.2.1", "os": "android", "picScale": "16", "h": "3310"}

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    def start_requests(self):
        for a in self.keywords.keys():
            for p in range(1, self.keywords[a] + 1):
                self.querystring['pageNo'] = str(p)
                self.querystring['words'] = a
                url = 'https://api.k.sohu.com/api/search/v5/search.go?' + helper.getUrlWithPars(self.querystring)
                yield Request(url=url, callback=self.parse, headers=self.headers, dont_filter=True)


    def parse(self, response):
        data = json.loads(response.text)
        if "msg" in data.keys():
            if data['msg'] == 'empty data list':return
        for i in data['resultList']:
            author = i['media']
            id = i['newsId']
            linkUrl = 'https://3g.k.sohu.com/t/n{}?showType='.format(str(id))
            title = i['title']
            # 发布时间
            timeStamp = float(int(i['time']) / 1000)
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            pub_time = otherStyleTime

            # 更新时间
            # timeStamp2 = float(int(i['updateTime']) / 1000)
            # timeArray2 = time.localtime(timeStamp2)
            # otherStyleTime2 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray2)
            # updateTime = otherStyleTime2

            yield Request(url=linkUrl, callback=self.content_parse, headers=self.headers,
                          meta={'date': pub_time, 'title': title, 'id': id, 'author': author})

            # self.content_parse()


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
        pipleitem['S2'] = '搜狐新闻app'
        pipleitem['Q1'] = response.xpath('string(//div[@class="at-cnt-main"])').extract_first()
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
