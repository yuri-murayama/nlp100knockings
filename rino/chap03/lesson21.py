# -*- coding: utf-8 -*-

import re
from lesson20 import getEngland

article_England = getEngland()
article_England_list = article_England.split("\n")

for line in article_England_list:
   search_result = re.search("Category", line)
   if search_result:
      print(line)

"""
========
出力結果
========
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]

"""
