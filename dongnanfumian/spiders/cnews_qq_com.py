# -*- coding: utf-8 -*-
from lxml import etree
import time
import requests
import json
import scrapy
from scrapy import Request
from scrapy.conf import settings
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem


#天天快报
class CnewsQqComSpider(scrapy.Spider):
    name = 'cnews.qq.com'

    keywords = settings.get('KEYWORDS')

    headers = {
        # 'Host': 'r.cnews.qq.com',
        'Accept-Encoding': 'gzip,deflate',
        'Referer': 'http/cnews.qq.com/cnews/android/',
        'User-Agent': '%E5%A4%A9%E5%A4%A9%E5%BF%AB%E6%8A%A55010(android)',
        'Cookie': 'lskey=; luin=; skey=; uin=; logintype=0;',
        'qn-sig': '41b3aa487fc15c60686e86eb152abc87',
        'svqn': '1_4',
        'qn-rid': 'ccdac28e-44bd-476b-9601-d694a309e641',
        'snqn': 'qyrz7hgmkAlw33VtlM6CsKMFq9bwLW8yr3OwdthBuUACpC3S9+K1FAx9qXisLOgh4LAS50B6xYWSWOMSFDBkVI82sWWpMcu+hNsphLNnxfoMKt3jvgJz/Z9bwb2uJoMzUgu8qgIfJlfm4Osp9dIHgg==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Content-Length': '1247'
    }

    payload = {
        'REQBuildTime': '1551937615446',
        'omgbizid': '4b832e121d19714484fb493432fdc5c7813d0080214207',
        'bssid': '50:fa:84:50:89:b8',
        'commonIsFirstLaunch': '0',
        'source': '',
        'imsi': '',
        'currentTab': 'kuaibao',
        'type': 'aggregate',
        'ssid ': 'LIMR',
        'qimei': 'a000009114f247',
        'lastCheckCardType': '0',
        'curChannel': 'daily_timeline',
        'imsi_history': '0',
        'qn-sig': '41b3aa487fc15c60686e86eb152abc87',
        'REQExecTime': '1551937615447',
        'picSizeMode': '0',
        'curTab': 'kuaibao',
        'Cookie': '&lskey=&luin=&skey=&uin=&logintype=0',
        'kingCardType': '0',
        'adcode': '440104',
        'chlid': '',
        'query': '东风',  # 关键字
        'proxy_addr': '192.168.0.114:28888',
        'qn-rid': 'ccdac28e-44bd-476b-9601-d694a309e641',
        'omgid': '40dea49f00a327406a6a57f1eef0db6ed2cf0010213a16',
        'activefrom': 'icon',
        'muid': '411537045290995458',
        'commonsid': '1f19a69c2f7f41a4bac150f608f663a3',
        'qqnetwork': 'wifi',
        'unixtimesign': '1551937615453',
        'commonGray': '1_3|2_0|12_1|49_1|14_1|17_1|30_1',
        'page': '2',  # 页数
        'rawQuery': '',
        'is_wap': '0',
        'devid': 'A000009114F247',
        'screen_width': '720',
        'appver': '27_areading_5.0.10',
        'apptype': 'android',
        'mid': 'e8023ec8e0ad0fcd40d79dae81171e361cb4a062',
        'appversion': '5.0.10',
        'store': '9001087',
        'hw_fp': 'HONOR/DUA-AL00/HWDUA-M:8.1.0/HONORDUA-AL00/1.0.0.160(C00):user/release-keys',
        'mac': 'B8:94:36:14:B3:14',
        'hw': 'HUAWEI_DUA-AL00',
        'uid': 'c4917cf1df8f108a',
        'screen_height': '1356',
        'origin_imei': 'A000009114F247',
        'sceneid': '',
        'android_id': 'c4917cf1df8f108a'
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

    # def start_requests(self):
    #     for i in self.keywords.keys():
    #         for j in range(self.keywords[i]):
    #             self.payload['query'] = i
    #             self.payload['page'] = str(j)
    #             url = "https://r.cnews.qq.com/searchByType?devid=A000009114F247"
    #             resb = requests.post(url=url, data=self.payload, headers=self.headers)
    #             time.sleep(2)
    #             body = json.loads(resb.text)
    #             for i in body['new_list']['data']:
    #                 if 'article' in i.keys():
    #                     id = i['article']['id']
    #                     date = i['article']['time']
    #                     title = i['article']['title']
    #                     author = i['article']['source']
    #                     time.sleep(1)
    #                     if 'url' in i['article'].keys():
    #                         resb2 = requests.post(url=i['article']['url'])
    #                         pipleitem = DongnanfumianItem()
    #                         selector = etree.HTML(resb2.text)
    #                         pipleitem['S6'] = date
    #                         pipleitem['S0'] = id
    #                         pipleitem['S1'] = i['article']['url']
    #                         pipleitem['S4'] = title
    #                         pipleitem['S3a'] = '文章'
    #                         pipleitem['G1'] = author
    #                         pipleitem['S3d'] = None
    #                         pipleitem['S7'] = "APP"
    #                         pipleitem['S2'] = '天天快报'
    #                         pipleitem['Q1'] = selector.xpath('string(//div[@class="content-box"])')
    #                         pipleitem['S5'] = helper.get_localtimestamp()
    #
    #                         print(pipleitem)
                            # return pipleitem

    def start_requests(self):
        for i in self.keywords.keys():
            for j in range(self.keywords[i]):
                self.payload['query'] = i
                self.payload['page'] = str(j)
                url = "https://r.cnews.qq.com/searchByType?devid=A000009114F247"
                resb = requests.post(url=url, data=self.payload, headers=self.headers)
                body = json.loads(resb.text)
                for i in body['new_list']['data']:
                    if 'article' in i.keys():
                        id=date=title=author=None
                        if 'id' in i['article'].keys():id = i['article']['id']
                        if 'time' in i['article'].keys():date = i['article']['time']
                        if 'title' in i['article'].keys():title = i['article']['title']
                        if 'source' in i['article'].keys():author = i['article']['source']
                        if 'url' in i['article'].keys():
                            yield Request(url=i['article']['url'],callback=self.content_parse,headers=self.headers,
                                          meta={'id':id,'date':date,'title':title,'author':author})

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
        pipleitem['S2'] = '天天快报'
        pipleitem['Q1'] = response.xpath('string(//div[@class="content-box"])').extract()
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
        # print(pipleitem)