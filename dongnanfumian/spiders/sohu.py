# -*- coding: utf-8 -*-
import re
import json,time
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import FormRequest
from scrapy_splash import SplashRequest

# 搜狐新闻app  {"code":91000,"msg":"empty data list"} 没数据
class EeoComCnSpider(scrapy.Spider):
    name = 'api.k.sohu.com'
    allowed_domains = ['https://api.k.sohu.com/api/search/v5/search.go']

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
                entry_point = 'https://api.k.sohu.com/api/search/v5/search.go?rt=json&pageNo={p}&words={k}&pageSize=20&' \
                              'type=0&gid=x011060802ff0f509854f181600023703a473ca12949&apiVersion=42&sid=10&u=1&keyfrom=input&refertype=' \
                              '1&versionName=6.2.1&os=android&picScale=16&h=3310'.format(k=a, p=p)
                #entry_point = 'http://app.time-weekly.com/timefinance/news/search/net?keyword={k}&page={p}&pageSize=10&muid=A000009114F247&actionSource=1'.format(k=a, p=p)
                yield SplashRequest(url=entry_point, callback=self.parse, splash_headers=self.headers, dont_filter=True, endpoint='execute', args={'lua_source': self.script1})


    def parse(self, response):


        data = json.loads(response.text)

        for i in data['resultList']:

            self.media = i['media']
            self.newsId = i['newsId']

            self.linkUrl = 'https://3g.k.sohu.com/t/n'+ str(i['newsId']) +'?showType='

            self.title = i['title']
            # 发布时间
            timeStamp = float(int(i['time']) / 1000)
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            self.pub_time = otherStyleTime
            # 更新时间
            timeStamp2 = float(int(i['updateTime']) / 1000)
            timeArray2 = time.localtime(timeStamp2)
            otherStyleTime2 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray2)
            self.updateTime = otherStyleTime2
            self.content_parse()
    def  content_parse(self):

        pipleitem = DongnanfumianItem()

        pipleitem['id'] =  self.newsId
        pipleitem['title'] = self.title
        pipleitem['linkUrl'] = self.linkUrl
        pipleitem['media'] = self.media
        pipleitem['pub_time'] = self.pub_time
        pipleitem['updateTime'] = self.updateTime

        return pipleitem



