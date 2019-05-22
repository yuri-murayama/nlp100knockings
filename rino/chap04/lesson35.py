# -*- coding: utf-8 -*-

from lesson30 import getNekoMecab

neko_list = getNekoMecab()

i = 0
while i < len(neko_list):
    if neko_list[i]["pos"] == "名詞":
        i_next = i+1

        while neko_list[i_next]["pos"] == "名詞":
            if i_next == i+1:
                print("\n"+neko_list[i]["surface"], end="")

            print(neko_list[i_next]["surface"], end="")
            i_next += 1

        i = i_next

    else:
        i += 1

"""
========
出力結果
========

人間中
一番獰悪
時妙
一毛
その後猫
一度
...

"""
