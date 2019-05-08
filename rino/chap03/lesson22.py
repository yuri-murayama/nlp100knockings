# -*- coding: utf-8 -*-

import re
from lesson20 import getEngland

article_England = getEngland()
article_England_list = article_England.split("\n")

for line in article_England_list:
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category_line is not None:
        print(category_line.group(1))

"""
========
出力結果
========
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国
1801年に設立された州・地域

"""
