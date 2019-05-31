# -*- coding: utf-8 -*-

CABOCHA_PATH = "./neko.txt.cabocha"

class Morph:
    def __init__(self, line):
        tab_list = line.split("\t")
        self.surface = tab_list[0]
        self.base = tab_list[1].split(",")[6]
        self.pos = tab_list[1].split(",")[0]
        self.pos1 = tab_list[1].split(",")[1]

def getNekoCabocha():
    neko_morph_all = []
    neko_morph_bysentence = []

    with open(CABOCHA_PATH) as f:
        for line in f:

            if (line != "EOS\n") and (line[0] != "*"):
                neko_morph = Morph(line)
                neko_morph_bysentence.append(neko_morph)

            elif line == "EOS\n":
                neko_morph_all.append(neko_morph_bysentence)
                neko_morph_bysentence = []

            else:
                pass

    return neko_morph_all

if __name__ == "__main__":
    neko_list = getNekoCabocha()
    for word_info in neko_list[2]:
        print("surface:{}, base:{}, pos:{}, pos1:{}".format(word_info.surface,
                                                            word_info.base,
                                                            word_info.pos,
                                                            word_info.pos1))

"""
========
出力結果
========

surface:　, base:　, pos:記号, pos1:空白
surface:吾輩, base:吾輩, pos:名詞, pos1:代名詞
surface:は, base:は, pos:助詞, pos1:係助詞
surface:猫, base:猫, pos:名詞, pos1:一般
surface:で, base:だ, pos:助動詞, pos1:*
surface:ある, base:ある, pos:助動詞, pos1:*
surface:。, base:。, pos:記号, pos1:句点

"""
