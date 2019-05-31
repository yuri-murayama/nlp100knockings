# -*- coding: utf-8 -*-

from lesson41 import getNekoChunk

neko_list = getNekoChunk()

for sentence in neko_list:
    for i in range(len(sentence)):
        for chunk in sentence:
            if int(chunk.dst) == i:
                chunk_pos_list = [m.pos for m in chunk.morphs]
                sentence_pos_list = [mm.pos for mm in sentence[i].morphs]

                if ((("名詞" in chunk_pos_list) and ("動詞" in sentence_pos_list))
                or
                (("動詞" in chunk_pos_list) and ("名詞" in sentence_pos_list))):
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

　どこで	生れたか

見当が	つかぬ

じめじめした	所で

所で	泣いて

ニャーニャー	泣いて

泣いて	記憶している

いた事だけは	記憶している

ここで	始めて

始めて	人間という

吾輩は	見た

ものを	見た

あとで	聞くと

"""
