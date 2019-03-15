# -*- coding: utf-8 -*-
import json
import scrapy
import requests
from dongnanfumian import helper
from dongnanfumian.items import DongnanfumianItem
from scrapy import Request
from scrapy.conf import settings


class InewsQqComSpider(scrapy.Spider):
    name = 'inews.qq.com'

    keywords = settings.get('KEYWORDS')

    headers = {
        'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 8.1.0; DUA-AL00 Build/HUAWEI)',
        'Referer': 'http://inews.qq.com/inews/android/'
    }

    data = {
        'launchSearchFrom':'btn',
        'isDefault':'0',
        'cp_type':'0',
        'query':'思域',
        'searchTag':'思域',
        'disable_qc':'0',
        'search_type':'all',
        'searchStartFrom':'header',
        'net_proxy':'DIRECT',
        'rom_type':'EMUI%20EmotionUI_8.0.0',
        'currentChannelId':'news_news_top',
        'omgbizid':'71f6cc6d1a2360463b28b90803a8487ff5bc0050213a16',
        'mid':'d38dbd4bfef577eda04469a8ff742244ececd6ab',
        'real_device_width':'2.55',
        'mac':'B8%3A94%3A36%3A14%3AB3%3A14',
        'hw':'HUAWEI_DUA-AL00',
        'isoem':'0',
        'screen_height':'1356',
        'is_special_device':'0',
        'imsi_history':'0',
        'origin_imei':'A000009114F247',
        'global_info':'1%7C1%7C1%7C1%7C1%7C13%7C7%7C1%7C0%7C6%7C1%7C1%7C2%7C%7C0%7CJ309P000000000%3AJ601P000000000%3AJ401P000000000%3AJ401P100000000%3AJ304P000000000%3AJ064P000000000%3AA267P000023501%3AJ060P000000000%3AJ060P008000000%3AJ060P009000000%3AJ055P000000000%3AA402P000041202%3AA402P005047201%3AA054P000044602%3AJ054P100000000%7C1411%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C1001%7C0%7C0%7C1%7C1%7C1%7C1%7C1%7C1%7C-1%7C0%7C0%7C5%7C2%7C0%7C0%7C0%7C5%7C0%7C0%7C1%7C0%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C1%7C0%7C1%7C1%7C0%7C0%7C1%7C2%7C0%7C0%7C1%7C2',
        'net_slot':'0',
        'dpi':'320.0',
        'pagestartfrom':'icon',
        'screen_width':'720',
        'adcode':'440104',
        'apptype':'android',
        'store':'96',
        'net_apn':'0',
        'real_device_height':'5.1',
        'islite':'0',
        'activefrom':'icon',
        'isElderMode':'0',
        'global_session_id':'1551945866940',
        'origCurrentTab':'top',
        'is_chinamobile_oem':'0',
        'net_bssid':'50%3Afa%3A84%3A50%3A89%3Ab8',
        'qqnetwork':'wifi',
        'network_type':'wifi',
        'currentTabId':'news_news',
        'startTimestamp':'1551945943'
    }

    entry_point = 'https://r.inews.qq.com/search?search_from=&devid=1099ffec2ca12181&qimei=1099ffec2ca12181&uid=1099ffec2ca12181&appver=27_android_5.7.60&omgid=40dea49f00a327406a6a57f1eef0db6ed2cf0010213a16&Cookie=lskey%3D;skey%3D;uin%3D;%20luin%3D;logintype%3D0;%20main_login%3D;%20&qn-sig=5cf9c766fbcb620e4f934d085e4f9ba6&qn-rid=ca5a3797-a3cf-4ae9-8c93-df041a197e8c'

    def start_requests(self):
        for i in self.keywords.keys():
            self.data['query'] = i
            self.data['searchTag'] = i
            res = requests.post(url=self.entry_point, data=self.data, headers=self.headers)
            body = json.loads(res.text)
            if len(body['secList']) == 0: return
            for item in body['secList']:
                if 'newsList' not in item.keys():continue
                item = item['newsList'][0]
                id=title=date=content=author=None
                if 'url' not in item.keys():continue
                if 'id' in item.keys():id = item['id']
                if 'title' in item.keys():title = item['title']
                if 'time' in item.keys():date = item['time']
                if 'source' in item.keys():author = item['source']
                if 'abstract' in item.keys():content = item['abstract']
                yield Request(url=item['url'], callback=self.content_parse, headers=self.headers,
                              meta={'id': id, 'title': title, 'date': date, 'author': author,'content':content})

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
        pipleitem['S2'] = '腾讯新闻app'
        # pipleitem['Q1'] = response.xpath('string(//div[@class="_1Xa3FHZJUzr6lzb4nMjOa4"])').extract_first()
        pipleitem['Q1'] = response.meta['content']
        pipleitem['S5'] = helper.get_localtimestamp()

        return pipleitem
