# -*- coding: utf-8 -*-
import re
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import FormRequest,Request
from scrapy_splash import SplashRequest

#经济观察网
class EeoComCnSpider(scrapy.Spider):
    name = 'eeo.com.cn'
    allowed_domains = ['eeo.com.cn']

    entry_point = {
        '首页':'http://www.eeo.com.cn/'
    }

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

    def start_requests(self):
        for key in self.entry_point.keys():
            yield Request(url=self.entry_point[key], callback=self.parse, headers=self.headers, dont_filter=True)
            # yield SplashRequest(url=self.entry_point[key], callback=self.parse, splash_headers=self.headers, dont_filter=True, endpoint='execute', args={'lua_source': self.script1})

    def parse(self, response):
        links = response.css('a::attr(href)').extract()
        if len(links) == 0: return
        for link in set(links):  # 转成set集合，去重
            if re.search('(http|https)://www.eeo.com.cn/[/\d]+', link):
                yield Request(url=link, callback=self.parse, headers=self.headers)
                # yield SplashRequest(url=suburl, callback=self.content_parse, splash_headers=self.headers,
                #                     dont_filter=True, endpoint='execute', args={'lua_source': self.script2})

    def content_parse(self, response):
        pipleitem = DongnanfumianItem()

        pipleitem['date'] = response.css('.xd-b-b p span::text').extract_first()
        pipleitem['id'] = re.findall('/(\d{5,})', response.url)[0]
        pipleitem['url'] = response.url
        pipleitem['title'] = response.css('head title::text').extract_first()
        pipleitem['type'] = '文章'
        pipleitem['author'] = None
        pipleitem['natvigate'] = None
        pipleitem['platform'] = "PC"
        pipleitem['webname'] = '经济观察网'
        pipleitem['content'] = response.xpath('string(//div[@class="xx_boxsing"])').extract()
        pipleitem['crawl_time'] = helper.get_localtimestamp()

        return pipleitem
