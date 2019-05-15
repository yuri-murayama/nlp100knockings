# -*- coding: utf-8 -*-

import re
from lesson20 import getEngland
import urllib.request
import urllib.parse
import json

article_England = getEngland()
country_info = {}

kiso_pattern = r'^\{\{基礎情報(.*?)\}\}$'
kiso_match = re.findall(kiso_pattern, article_England, re.MULTILINE+re.DOTALL)

temp_pattern = r'^\|(.*?)\s=\s(.*?)\n'
temp_match = re.findall(temp_pattern, kiso_match[0], re.MULTILINE+re.DOTALL)

for (k, v) in temp_match:
    country_info[k] = v


url = 'https://ja.wikipedia.org/w/api.php?' \
      + 'action=query' \
      + '&format=json' \
      + '&titles=File:' + urllib.parse.quote(country_info["国旗画像"]) \
      + '&prop=imageinfo' \
      + '&iiprop=url'

with urllib.request.urlopen(url) as res:
    data = json.loads(res.read().decode())
    print(data['query']['pages']['-1']['imageinfo'][0]['url'])


"""
========
出力結果
========

https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg

"""
