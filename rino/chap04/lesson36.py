# -*- coding: utf-8 -*-

from lesson30 import getNekoMecab

def counterWord():
    neko_list = getNekoMecab()

    word_list = {}

    for neko in neko_list:
        w = neko['base']
        if w in word_list:
            word_list[w] += 1
        else:
            word_list[w] = 1

    # そーと
    count_sorted = sorted(word_list.items(), key=lambda x:x[1], reverse=True)
    return count_sorted

# print(counterWord())
"""
========
出力結果
========

[('の', 9194), ('。', 7486), ('て', 6848), ('、', 6772),
('は', 6420), ('に', 6243), ('を', 6071), ('だ', 5975),
('と', 5508), ('が', 5337), ('た', 4267), ('する', 3657),
('「', 3231), ('」', 3225), ('ない', 3052), ('も', 2479),
('ある', 2320), ('*\n', 2191), ('で', 2081), ('から', 2031), ('いる', 1777),
...

"""
