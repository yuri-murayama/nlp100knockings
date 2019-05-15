# -*- coding: utf-8 -*-
# 弱い強調: ''...''
# 強調: '''...'''
# 強い強調: ''''...''''

import re
from lesson20 import getEngland

article_England = getEngland()
country_info = {}

kiso_pattern = r'^\{\{基礎情報(.*?)\}\}$'
kiso_match = re.findall(kiso_pattern, article_England, re.MULTILINE+re.DOTALL)

temp_pattern = r'^\|(.*?)\s=\s(.*?)\n'
temp_match = re.findall(temp_pattern, kiso_match[0], re.MULTILINE+re.DOTALL)

for (k, v) in temp_match:
    v = re.sub(r"'+", "", v)
    country_info[k] = v

for k, v in sorted(country_info.items(), key=lambda x: x[1]):
    print("key:{}".format(k))
    print("value:{}".format(v))
    print()



"""
========
出力結果
========

key:確立形態4
value:現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更

↓

key:確立形態4
value:現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
"""
