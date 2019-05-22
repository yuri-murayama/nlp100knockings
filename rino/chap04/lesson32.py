# -*- coding: utf-8 -*-

from lesson30 import getNekoMecab

neko_list = getNekoMecab()

for neko in neko_list:
    if neko['pos'] == "動詞":
        print(neko['base'])

"""
========
出力結果
========

生れる
つく
する
泣く
する
いる
始める
見る
聞く
...

"""
