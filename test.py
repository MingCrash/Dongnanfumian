# -*- encoding: utf-8 -*-
# Author: MingCrash
import requests
from dongnanfumian import helper

# keyword 关键字   page 页数
url = "http://app.time-weekly.com/timefinance/news/search/net"
querystring = {"keyword":"%E5%AE%9D%E9%A9%AC","page":"1","pageSize":"10","muid":"A000009114F247","actionSource":"1"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }

print('http://app.time-weekly.com/timefinance/news/search/net?'+helper.getUrlWithPars(querystring))

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)