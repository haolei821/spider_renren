# coding: utf-8

import requests
import json
import pandas as pd

# 用户主页的链接
url = 'http://status.renren.com/GetSomeomeDoingList.do?userId=358210045&curpage=0&_jcb=jQuery111104597700930935882_1513220994258&requestToken=-735448934&_rtk=9feaeef4&_=1513220994259'

# cookie需自己添加
headers = {
    'Cookie':,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}
response = requests.get(url,headers = headers).text
response
res = json.loads(response.lstrip("jQuery111104597700930935882_1513220994258(").rstrip(")'"))['doingArray']
# for i in res['doingArray']:
#     print(i['content'])
df = pd.DataFrame(res)
print(df)

