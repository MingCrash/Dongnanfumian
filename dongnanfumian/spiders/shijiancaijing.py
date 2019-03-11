# -*- coding: utf-8 -*-
import re
import json,time
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import FormRequest
from scrapy_splash import SplashRequest

#时间财经
class EeoComCnSpider(scrapy.Spider):
    name = 'app.time-weekly.com'
    allowed_domains = ['http://app.time-weekly.com/timefinance/news/search/net']

    productPage = {
        '东南汽车': 10
    }

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

    def start_requests(self):
        for a in self.productPage.keys():
            for p in range(1, self.productPage[a] + 1):
                entry_point = 'http://app.time-weekly.com/timefinance/news/search/net?keyword={k}&page={p}&pageSize=10&muid=A000009114F247&actionSource=1'.format(k=a, p=p)
                yield SplashRequest(url=entry_point, callback=self.parse, splash_headers=self.headers, dont_filter=True, endpoint='execute', args={'lua_source': self.script1})


    def parse(self, response):
        data = json.loads(response.text)
        for i in data['result']['list']:
            self.id= i['id']
            self.title = i['title']
            self.linkUrl = i['linkUrl']
            self.source = i['source']
            # 13位时间戳转换
            timeStamp = float(i['time'] / 1000)
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            self.pub_time = otherStyleTime
            self.content_parse()

    def  content_parse(self):

        pipleitem = DongnanfumianItem()

        pipleitem['id'] =  self.id
        pipleitem['title'] = self.title
        pipleitem['linkUrl'] = self.linkUrl
        pipleitem['source'] = self.source
        pipleitem['pub_time'] = self.pub_time

        return pipleitem

