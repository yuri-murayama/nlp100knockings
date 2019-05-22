# -*- coding: utf-8 -*-

from lesson30 import getNekoMecab

neko_list = getNekoMecab()

for neko in neko_list:
    if neko['pos'] == "動詞":
        print(neko['surface'])

"""
========
出力結果
========

生れ
つか
し
泣い
し
いる
始め
見
聞く
...

"""
