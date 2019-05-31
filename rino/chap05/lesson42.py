# -*- coding: utf-8 -*-

from lesson41 import getNekoChunk

neko_list = getNekoChunk()

for sentence in neko_list:
    for i in range(len(sentence)):
        for chunk in sentence:
            if int(chunk.dst) == i:
                for m in chunk.morphs:
                    print(m.surface.strip("。").strip("、").replace("「", "").replace("」", ""), end="")
                print("\t",end="")
                for mm in sentence[i].morphs:
                    print(mm.surface.strip("。").strip("、").replace("「", "").replace("」", ""), end="")
                print("\n")


"""
========
出力結果
========

　	猫である  # なぜか空白が入る...

吾輩は	猫である

名前は	無い

まだ	無い

　どこで	生れたか  # なぜか空白が入る...

生れたか	つかぬ

とんと	つかぬ

見当が	つかぬ

何でも	薄暗い

薄暗い	所で

じめじめした	所で

"""
