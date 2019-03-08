# -*- coding: utf-8 -*-
import re
import scrapy
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import FormRequest
from scrapy_splash import SplashRequest

#经济观察网
class EeoComCnSpider(scrapy.Spider):
    name = 'eeo.com.cn'
    allowed_domains = ['http://www.eeo.com.cn/']

    entry_point = {
        '首页':'http://www.eeo.com.cn/'
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
        for key in self.entry_point.keys():
            yield SplashRequest(url=self.entry_point[key], callback=self.parse, splash_headers=self.headers, dont_filter=True, endpoint='execute', args={'lua_source': self.script1})

    def parse(self, response):
        links = response.css('a::attr(href)').extract()
        if len(links) == 0: return
        for link in set(links):  # 转成set集合，去重
            if re.search('watch\?v=\S*', link):
                suburl = 'https://www.youtube.com/watch?' + re.findall('v=\S*.', link)[0]
                yield SplashRequest(url=suburl, callback=self.content_parse, splash_headers=self.headers,
                                    dont_filter=True, endpoint='execute', args={'lua_source': self.script2})

    def content_parse(self, response):
        date = response.xpath(
            '//span[@class="date style-scope ytd-video-secondary-info-renderer"]/text()').extract_first()
        if len(date) > 0:
            if helper.compare_time(helper.formatTime(date), self.limittime) < 0: return
        else:
            return

        pipleitem = DongnanfumianItem()

        pipleitem['date'] = helper.formatTime(date)
        pipleitem['id'] = re.findall('v=(\S*).', response.url)[0]
        pipleitem['url'] = response.url
        pipleitem['title'] = response.xpath('//div[@id="container"]/h1/yt-formatted-string/text()').extract_first()
        pipleitem['source'] = 'Youtube'
        pipleitem['editor'] = response.css('#owner-name a::text').extract_first()
        pipleitem['content'] = None
        pipleitem['image_urls'] = None
        pipleitem['video_urls'] = response.css('video::attr(src)').extract_first()
        pipleitem['share'] = None
        tmp = response.xpath('//yt-formatted-string[@id="text"]/@aria-label').extract()
        if len(tmp) < 2: tmp = ['0', '0']
        for i in range(len(tmp)):
            if re.search('No', tmp[i]): tmp[i] = '0'
        pipleitem['like'] = re.findall('\d*', tmp[0])[0]
        pipleitem['dislike'] = re.findall('\d*', tmp[1])[0]
        pipleitem['comment'] = \
        re.findall('\d*', response.xpath('//h2[@id="count"]/yt-formatted-string/text()').extract_first())[0]
        pipleitem['crawl_time'] = helper.get_localtimestamp()

        return pipleitem
