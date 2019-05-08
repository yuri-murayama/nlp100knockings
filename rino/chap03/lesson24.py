# -*- coding: utf-8 -*-

import re
from lesson20 import getEngland

article_England = getEngland()
article_England_list = article_England.split("\n")

for line in article_England_list:
    category_line_ja = re.search("^\[\[ファイル:(.*?)(|\|.*)+\]\]$", line)
    category_line_en = re.search("^\[\[File:(.*?)(|\|.*)+\]\]$", line)

    if category_line_ja is not None:
        print(category_line_ja.group(1))
    elif category_line_en is not None:
        print(category_line_en.group(1))

"""
========
出力結果
========
Battle of Waterloo 1815.PNG
The British Empire.png
Uk topo en.jpg
BenNevis2005.jpg
Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg
Palace of Westminster, London - Feb 2007.jpg
David Cameron and Barack Obama at the G20 Summit in Toronto.jpg
Soldiers Trooping the Colour, 16th June 2007.jpg
Scotland Parliament Holyrood.jpg
London.bankofengland.arp.jpg
City of London skyline from London City Hall - Oct 2008.jpg
Oil platform in the North SeaPros.jpg
Eurostar at St Pancras Jan 2008.jpg
Heathrow T5.jpg
Anglospeak.svg
CHANDOS3.jpg
The Fabs.JPG
Wembley Stadium, illuminated.jpg

"""
