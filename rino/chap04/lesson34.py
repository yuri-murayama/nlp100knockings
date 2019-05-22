# -*- coding: utf-8 -*-

from lesson30 import getNekoMecab

neko_list = getNekoMecab()

for i, neko in enumerate(neko_list):
    if (neko['surface'] == "の") and (neko['pos'] == "助詞"):
        if neko_list[i-1]['pos'] == "名詞" and neko_list[i+1]['pos'] == "名詞":
            print(neko_list[i-1]['surface']+"の"+neko_list[i+1]['surface'])

"""
========
出力結果
========

彼の掌
掌の上
書生の顔
はずの顔
顔の真中
穴の中
書生の掌
掌の裏
何の事
肝心の母親
...

"""
