# -*- coding: utf-8 -*-
import re
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import FormRequest,Request
from scrapy.conf import settings

#经济观察网
class EeoComCnSpider(scrapy.Spider):
    name = 'eeo.com.cn'
    allowed_domains = ['eeo.com.cn']

    entry_point = 'http://app.eeo.com.cn/?app=search&controller=index&action=searchall'

    keywords = settings.get('KEYWORDS')

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip',  # 只要gzip的压缩格式
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    data = {
        'w': '思域',
        '搜索': '搜索'
    }

    def start_requests(self):
        for i in self.keywords.keys():
            self.data['w'] = i
            yield FormRequest(url=self.entry_point.format(kw=i), formdata=self.data, callback=self.parse, headers=self.headers,
                                  dont_filter=True)

    def parse(self, response):
        links = response.css('.new_list a::attr(href)').extract()
        if len(links) == 0: return
        next = response.css('div[class*="wzlist_page"] a::attr(href)').extract_first()
        if next != None: yield Request(url=next, callback=self.parse, headers=self.headers,dont_filter=True)
        for link in set(links):  # 转成set集合，去重
            yield Request(url=link, callback=self.content_parse, headers=self.headers)

    def content_parse(self, response):
        pipleitem = DongnanfumianItem()

        pipleitem['S6'] = response.css('.xd-b-b p span::text').extract_first()
        pipleitem['S0'] = re.findall('/(\d{5,})', response.url)[0]
        pipleitem['S1'] = response.url
        pipleitem['S4'] = response.css('head title::text').extract_first()
        pipleitem['S3a'] = '文章'
        author = re.findall('(.*?)\d{4}', response.xpath('string(//div[@class="xd-b-b"]/p)').extract_first())[0]
        pipleitem['G1'] = author
        pipleitem['S3d'] = None
        pipleitem['S7'] = "PC"
        pipleitem['S2'] = '经济观察网'
        pipleitem['Q1'] = response.xpath('string(//div[@class="xx_boxsing"])').extract_first()
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
