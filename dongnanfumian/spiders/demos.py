# -*- encoding: utf-8 -*-

############## 天天快报
import requests,json
url = "https://r.cnews.qq.com/searchByType?devid=A000009114F247"
payloadHeader = {
    'Host':'r.cnews.qq.com',
    'Accept-Encoding':'gzip,deflate',
    'Referer':'http/cnews.qq.com/cnews/android/',
    'User-Agent':'%E5%A4%A9%E5%A4%A9%E5%BF%AB%E6%8A%A55010(android)',
    'Cookie':'lskey=; luin=; skey=; uin=; logintype=0;',
    'qn-sig':'41b3aa487fc15c60686e86eb152abc87',
    'svqn':'1_4',
    'qn-rid':'ccdac28e-44bd-476b-9601-d694a309e641',
    'snqn':'qyrz7hgmkAlw33VtlM6CsKMFq9bwLW8yr3OwdthBuUACpC3S9+K1FAx9qXisLOgh4LAS50B6xYWSWOMSFDBkVI82sWWpMcu+hNsphLNnxfoMKt3jvgJz/Z9bwb2uJoMzUgu8qgIfJlfm4Osp9dIHgg==',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'Keep-Alive',
    'Content-Length':'1247'
    }
payload = {
'REQBuildTime':'1551937615446',
'omgbizid':'4b832e121d19714484fb493432fdc5c7813d0080214207',
'bssid':'50:fa:84:50:89:b8',
'commonIsFirstLaunch':'0',
'source':'',
'imsi':'',
'currentTab':'kuaibao',
'type':'aggregate',
'ssid ':'LIMR',
'qimei':'a000009114f247',
'lastCheckCardType':'0',
'curChannel':'daily_timeline',
'imsi_history':'0',
'qn-sig':'41b3aa487fc15c60686e86eb152abc87',
'REQExecTime':'1551937615447',
'picSizeMode':'0',
'curTab':'kuaibao',
'Cookie':'&lskey=&luin=&skey=&uin=&logintype=0',
'kingCardType':'0',
'adcode':'440104',
'chlid':'',
'query':'东风',# 关键字
'proxy_addr':'192.168.0.114:28888',
'qn-rid':'ccdac28e-44bd-476b-9601-d694a309e641',
'omgid':'40dea49f00a327406a6a57f1eef0db6ed2cf0010213a16',
'activefrom':'icon',
'muid':'411537045290995458',
'commonsid':'1f19a69c2f7f41a4bac150f608f663a3',
'qqnetwork':'wifi',
'unixtimesign':'1551937615453',
'commonGray':'1_3|2_0|12_1|49_1|14_1|17_1|30_1',
'page':'2',# 页数
'rawQuery':'',
'is_wap':'0',
'devid':'A000009114F247',
'screen_width':'720',
'appver':'27_areading_5.0.10',
'apptype':'android',
'mid':'e8023ec8e0ad0fcd40d79dae81171e361cb4a062',
'appversion':'5.0.10',
'store':'9001087',
'hw_fp':'HONOR/DUA-AL00/HWDUA-M:8.1.0/HONORDUA-AL00/1.0.0.160(C00):user/release-keys',
'mac':'B8:94:36:14:B3:14',
'hw':'HUAWEI_DUA-AL00',
'uid':'c4917cf1df8f108a',
'screen_height':'1356',
'origin_imei':'A000009114F247',
'sceneid':'',
'android_id':'c4917cf1df8f108a'
}
r = requests.post(url, data=payload, headers=payloadHeader)
# print(r.content.decode('gbk'))
print(json.loads(r.text))


############## 新浪APP
# 完整链接
# http://newsapi.sina.cn/?resource=hbpage&newsId=HB-1-snhs/index-search&lq=1&page=1&newpage=0&keyword=%25E4%25B8%259C%25E9%25A3%258E%25E6%25B1%25BD%25E8%25BD%25A6&lDid=9b6647a6-d104-450e-b474-5d7363d77e3b&appVersion=7.11.1&oldChwm=&city=CHXX0037&loginType=0&authToken=fa58dd43d2916ed0561dc05dc188641a&link=&authGuid=6509310653105356298&ua=HUAWEI-DUA-AL00__sinanews__7.11.1__android__8.1.0&deviceId=e4f479caa6680ca7&connectionType=2&resolution=720x1356&mac=02%3A00%3A00%3A00%3A00%3A00&weiboUid=&osVersion=8.1.0&chwm=14020_0001&weiboSuid=&andId=79498f50fbe8c81a&from=6000095012&sn=HFK9K18601475728&aId=01Au2MgsJiFYf0wpBEVkyBIh9iMZvpL4zJlgGH0pc1Ifad0Z0.&deviceIdV1=12fd468134b6ddf8&osSdk=27&abver=1551752314700110001&accessToken=&seId=14e7fcedbe&imei=null&deviceModel=HUAWEI__HONOR__DUA-AL00&location=23.132299%2C113.311645&authUid=0&urlSign=793e026813&rand=336
url = "http://newsapi.sina.cn/"
#  keyword 关键字 如东南汽车   page页数
querystring = {"resource":"hbpage","newsId":"HB-1-snhs/index-search","lq":"1","page":"1","newpage":"0","keyword":"%25E4%25B8%259C%25E9%25A3%258E%25E6%25B1%25BD%25E8%25BD%25A6","lDid":"9b6647a6-d104-450e-b474-5d7363d77e3b","appVersion":"7.11.1","oldChwm":"","city":"CHXX0037","loginType":"0","authToken":"fa58dd43d2916ed0561dc05dc188641a","link":"","authGuid":"6509310653105356298","ua":"HUAWEI-DUA-AL00__sinanews__7.11.1__android__8.1.0","deviceId":"e4f479caa6680ca7","connectionType":"2","resolution":"720x1356","mac":"02%3A00%3A00%3A00%3A00%3A00","weiboUid":"","osVersion":"8.1.0","chwm":"14020_0001","weiboSuid":"","andId":"79498f50fbe8c81a","from":"6000095012","sn":"HFK9K18601475728","aId":"01Au2MgsJiFYf0wpBEVkyBIh9iMZvpL4zJlgGH0pc1Ifad0Z0.","deviceIdV1":"12fd468134b6ddf8","osSdk":"27","abver":"1551752314700110001","accessToken":"","seId":"14e7fcedbe","imei":"null","deviceModel":"HUAWEI__HONOR__DUA-AL00","location":"23.132299%2C113.311645","authUid":"0","urlSign":"793e026813","rand":"336"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    'cache-control': "no-cache",
    'Postman-Token': "831b41f5-900b-4c09-be6b-407575cde969"
    }
response = requests.get( url, headers=headers, params=querystring)
print(response.text)


############## 搜狐新闻app
# 完整链接
# https://api.k.sohu.com/api/search/v5/search.go?rt=json&pageNo=2&words=%E5%AE%9D%E9%A9%AC&p1=NjUwOTMxNTExMjU1NjczNjUzOA%3D%3D&pageSize=20&type=0&gid=x011060802ff0f509854f181600023703a473ca12949&apiVersion=42&sid=10&u=1&keyfrom=input&refertype=1&versionName=6.2.1&os=android&picScale=16&h=3310
# url = "https://api.k.sohu.com/api/search/v5/search.go"
# #  pageNo == 页数      words == 关键字 如东南汽车
# querystring = {"rt":"json","pageNo":"2","words":"%E5%AE%9D%E9%A9%AC","p1":"NjUwOTMxNTExMjU1NjczNjUzOA%3D%3D","pageSize":"20","type":"0","gid":"x011060802ff0f509854f181600023703a473ca12949","apiVersion":"42","sid":"10","u":"1","keyfrom":"input","refertype":"1","versionName":"6.2.1","os":"android","picScale":"16","h":"3310"}
# headers = {
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
#     }
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)


##############懂车帝APP
#keyword 关键字    offset 设置翻页    get
#https://is.snssdk.com/motor/search/api/2/wap/search_content/?from=news&keyword=%E4%B8%9C%E9%A3%8E&iid=65338592844&device_id=59868348056&ac=wifi&channel=huawei&aid=36&app_name=automobile&version_code=438&ab_client=a1%252Cc2%252Ce2%252Cf1%252Cg2%252Cf7&abflag=3&device_type=DUA-AL00&device_brand=HONOR&language=zh&os_api=27&os_version=8.1.0&uuid=A000009114F247&openudid=81e754ddcf1f3217&manifest_version_code=438&resolution=720*1356&dpi=320&update_version_code=4385&_rticket=1551863263302&search_sug=1&forum=1&cur_tab=1&motor_source=global&search_mode=common&city_name=%25E5%25B9%25BF%25E5%25B7%259E&gps_city_name=%25E5%25B9%25BF%25E5%25B7%259E&fp=PrTrLWctczc7FlwILSU1F2USP2Z7&as=A1A54CB7AF28DE1&cp=5C7F781DFE211E1&count=10&format=json&offset=20&search_from=h5&req_type=native&extra_params=%257B%257D&price_range=-1
# url = "https://is.snssdk.com/motor/search/api/2/wap/search_content/"
# querystring = {"from":"news","keyword":"%E4%B8%9C%E9%A3%8E","iid":"65338592844","device_id":"59868348056","ac":"wifi","channel":"huawei","aid":"36","app_name":"automobile","version_code":"438","ab_client":"a1%252Cc2%252Ce2%252Cf1%252Cg2%252Cf7","abflag":"3","device_type":"DUA-AL00","device_brand":"HONOR","language":"zh","os_api":"27","os_version":"8.1.0","uuid":"A000009114F247","openudid":"81e754ddcf1f3217","manifest_version_code":"438","resolution":"720%2A1356","dpi":"320","update_version_code":"4385","_rticket":"1551863263302","search_sug":"1","forum":"1","cur_tab":"1","motor_source":"global","search_mode":"common","city_name":"%25E5%25B9%25BF%25E5%25B7%259E","gps_city_name":"%25E5%25B9%25BF%25E5%25B7%259E","fp":"PrTrLWctczc7FlwILSU1F2USP2Z7","as":"A1A54CB7AF28DE1","cp":"5C7F781DFE211E1","count":"10","format":"json","offset":"20","search_from":"h5","req_type":"native","extra_params":"%257B%257D","price_range":"-1"}
# headers = {
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
#     }
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)


############## 老司机APP
# url = 'http://api.laosiji.com/search/ywf/indexapi/4/5/?md5=577eae7a94612ebf0593f9a25bdb24ce&production=laosiji&production_version=android3.3.1&systemtag=4&mac_address=02%3A00%3A00%3A00%3A00%3A00&appid=android&osversion=8.1.0&chargestatus=0&latitude=4.9E-324&longitude=4.9E-324&country=null&province=null&city=null&district=null&electricity=91%25&imsi=null&impresstime=1551972553364&ip=192.168.0.239&language=zh_CN&platform=2&version=2.2.5&screen_width=720&screen_hight=1356&brand=HONOR&devicename=DUA-AL00&deviceid=890b39fcc09aac6d60db1ed624169839&imei=A000009114F247&android=77a40ebc52d4b47f&local=GMT%2B08%3A00&lan=wifi&wifi=%22LIMR%22&wifi_address=192.168.0.1&pvuid=&uid=9169644&mobile=&operator=4&landscape=0&channel=HuaWei&winlog=&referer=app_selected_0%3Findex%3D0&page=app_search%3Fkeyword%3D%E4%B8%9C%E9%A3%8E%26cityid%3D131&snsid=&resourceid=&resourcetype=&adid=&seat=&startime=&endtime=&read_percent=&video_percent=&elapsed_time=&interfaceurl=&resultcode=&errormsg=&launchidentifying=2b1cc513-014f-4aa2-8ce3-5a0b79a03396&switchidentifying=8315e431-d6e8-4b01-8ff5-bd68a7a38e52&pageidentifying=e847ab75-1b27-4f03-b86d-af311e1e65bb&baseexpanded=%7B%22search%22%3A%22%E4%B8%9C%E9%A3%8E%22%2C%22cityid%22%3A%22131%22%2C%22type%22%3A%221%22%7D&baseattach=did%3D%26req_serial%3D53%26android_osbersion%3D27'
#
# payload= {
# 'parameter':'{"devicemarkjg":"140fe1da9eef9415479","search":"东风","devicemark":"AgR_pDZ43uTdv8Okzh9U5x4C-XjbqQ4_mAEO3PwgTlws","devicemarkopen":"1","cityid":"131","time":"2019-03-07 15:29:13","type":"1","devicemarkjgopen":"1","usertoken":"MnlPWTJFV04xT1RHVEUwTk9NamsyTm1OalF6SjVORk5OOHpOT0dHUXpsTU9UZD1aak9UbT1saE1sTm1FNU9FTkRGRzBpTkc1RU15T0dGR0prVFlaVFZ6WWxNR1oyUTVaVk9HTTJUTlltVTBFMFlXR1RZME5sWVRNME9sTW1KWlZmWXpGV1k1TURZVGxoTmxORFlFWT04Sg=="}',
# 'chk': '22eff5413726d9f613c476fa1c17ddfa'
#
# }
# payloadHeader = {
# 'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 8.1.0; DUA-AL00 Build/HUAWEI)'
# }
# r = requests.post(url, data=payload, headers=payloadHeader)
# print(json.loads(r.text))

########### 时代财经APP
# http://app.time-weekly.com/timefinance/news/search/net?keyword=宝马&page=2&pageSize=10&muid=A000009114F247&actionSource=1
# keyword 关键字   page 页数
url = "http://app.time-weekly.com/timefinance/news/search/net"
querystring = {"keyword":"%E5%AE%9D%E9%A9%AC","page":"1","pageSize":"10","muid":"A000009114F247","actionSource":"1"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

