# -*- coding: utf-8 -*-

from lesson41 import getNekoChunk

OUTPUT_TXT = "./output48.txt"
f = open(OUTPUT_TXT, "w")

neko_chunk_list = getNekoChunk()

for sentence in neko_chunk_list:
    for a_chunk in sentence:
        if "名詞" in [m.pos for m in a_chunk.morphs]:
            text = "".join([m.surface for m in a_chunk.morphs])

            dst = a_chunk.dst

            while 1:

                if dst == -1:
                    f.write(text + "\n")
                    break

                next_chunk = sentence[dst]
                text += " -> "
                text += "".join([m.surface for m in next_chunk.morphs])
                dst = next_chunk.dst

f.close()

"""
========
出力結果
========

# TODO: 句読点を削除しなきゃ、、、

吾輩は -> 見た。
ここで -> 始めて -> 人間という -> ものを -> 見た。
人間という -> ものを -> 見た。
ものを -> 見た。


"""
