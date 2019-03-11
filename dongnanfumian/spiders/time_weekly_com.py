# -*- coding: utf-8 -*-
import re
import json
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import FormRequest,Request
from scrapy_splash import SplashRequest

#时代财经APP
class TimeWeeklyComSpider(scrapy.Spider):
    name = 'time-weekly.com'

    entry_point = {
        '首页': 'http://www.eeo.com.cn/'
    }

    keywords = [

    ]

    # 使用splash时候记得加上
    # http_user = 'user'
    # http_pass = 'userpass'

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    script1 = """
                     function main(splash, args)
                       splash.images_enabled = false
                       splash.plugins_enabled = false
                       splash.html5_media_enabled = false
                       assert(splash:go(splash.args.url))
                       assert(splash:wait(3))
                       splash.scroll_position = {y=1500}
                       assert(splash:wait(3))
                       splash.scroll_position = {y=3000}
                       assert(splash:wait(3))
                       return splash:html()
                     end
                     """

    script2 = """
                     function main(splash, args)
                       splash.images_enabled = false
                       splash.plugins_enabled = false
                       splash.html5_media_enabled = false
                       assert(splash:go(splash.args.url))
                       assert(splash:wait(2))
                       splash.scroll_position = {y=300}
                       assert(splash:wait(4))
                       return splash:html()
                     end
                     """

    entry_point = 'http://app.time-weekly.com/timefinance/news/search/net?keyword={kw}&page={offset}&pageSize=40&muid=A000009114F247&actionSource=1'

    def start_requests(self):
        for i in self.keywords:
            for j in range(10):
                yield Request(url=self.entry_point.format(kw=i, offset=j), callback=self.parse, headers=self.headers,
                              dont_filter=True)
            # yield SplashRequest(url=self.entry_point[key], callback=self.parse, splash_headers=self.headers, dont_filter=True, endpoint='execute', args={'lua_source': self.script1})

    def parse(self, response):
        body = json.loads(response.text)
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

        pipleitem['date'] = response.meta['date']
        pipleitem['id'] = response.meta['id']
        pipleitem['url'] = response.url
        pipleitem['title'] = response.meta['title']
        pipleitem['type'] = '文章'
        pipleitem['author'] = response.meta['author']
        pipleitem['natvigate'] = None
        pipleitem['platform'] = "APP"
        pipleitem['webname'] = '时代财经APP'
        pipleitem['content'] = re.findall('content:([\S\s]*?)groupId:', response.text)[0]
        pipleitem['crawl_time'] = helper.get_localtimestamp()

        return pipleitem