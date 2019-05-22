# -*- coding: utf-8 -*-

from lesson30 import getNekoMecab

neko_list = getNekoMecab()

for neko in neko_list:
    if neko['pos1'] == "サ変接続":
        print(neko['surface'])

"""
========
出力結果
========

見当
記憶
話
装飾
突起
運転
記憶
分別
決心
我慢
...

"""
