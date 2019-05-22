# -*- coding: utf-8 -*-
# 素性：品詞, 品詞細分類1, 品詞細分類2, 品詞細分類3, 活用型(ctype), 活用形(cform), 原形, 読み, 発音
# 例：ある \t 助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル


MECAB_PATH = "./neko.txt.mecab"

def getNekoMecab():
    neko_dict_list = []
    with open(MECAB_PATH) as f:
        for line in f:

            if line == "EOS\n":
                continue

            tab_list = line.split("\t")
            surface = tab_list[0]
            base = tab_list[1].split(",")[6]
            pos = tab_list[1].split(",")[0]
            pos1 = tab_list[1].split(",")[1]
            neko_dict = {"surface": surface,
                         "base": base,
                         "pos" : pos,
                         "pos1": pos1 }
            neko_dict_list.append(neko_dict)

    return neko_dict_list

#print(getNekoMecab())

"""
========
出力結果
========

[{'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '数'},
{'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '空白'},
{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'},
{'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '係助詞'},
{'surface': '猫', 'base': '猫', 'pos': '名詞', 'pos1': '一般'},
{'surface': 'で', 'base': 'だ', 'pos': '助動詞', 'pos1': '*'}, ...

"""
