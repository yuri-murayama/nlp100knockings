# -*- coding: utf-8 -*-

import re
from lesson20 import getEngland

article_England = getEngland()
article_England_list = article_England.split("\n")

for line in article_England_list:
    line_level3 = re.search("^====(.*?)====$", line)
    line_level2 = re.search("^===(.*?)===$", line)
    line_level1 = re.search("^==(.*?)==$", line)
    if line_level3 is not None:
        print("{} level:3".format(line_level3.group(1)))

    elif line_level2 is not None:
        print("{} level:2".format(line_level2.group(1)))

    elif line_level1 is not None:
        print("{} level:1".format(line_level1.group(1)))

"""
========
出力結果
========
国名 level:1
歴史 level:1
地理 level:1
気候 level:2
政治 level:1
外交と軍事 level:1
地方行政区分 level:1
主要都市 level:2
科学技術 level:1
経済 level:1
鉱業 level:2
農業 level:2
貿易 level:2
通貨 level:2
企業 level:2
交通 level:1
道路 level:2
鉄道 level:2
海運 level:2
航空 level:2
通信 level:1
国民 level:1
言語 level:2
宗教 level:2
 婚姻  level:2
教育 level:2
文化 level:1
食文化 level:2
文学 level:2
 哲学  level:2
音楽 level:2
イギリスのポピュラー音楽 level:3
映画 level:2
コメディ level:2
国花 level:2
世界遺産 level:2
祝祭日 level:2
スポーツ level:1
サッカー level:2
競馬 level:2
モータースポーツ level:2
脚注 level:1
関連項目 level:1
外部リンク level:1

"""
