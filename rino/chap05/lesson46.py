# -*- coding: utf-8 -*-

from lesson41 import getNekoChunk

OUTPUT_TXT = "./output46.txt"
f = open(OUTPUT_TXT, "w")

neko_chunk_list = getNekoChunk()

for sentence in neko_chunk_list:
    for a_chunk in sentence:
        for a_morph in a_chunk.morphs:

            if a_morph.pos == "動詞":
                verb = a_morph.base
                joshi_list = []
                joshiword_list = []  # add

                for chunk_ind in a_chunk.srcs:
                    # morphの最後が助詞のため最後のみ取得
                    last_morph = sentence[chunk_ind].morphs[-1]
                    if last_morph.pos == "助詞":
                        joshi_list.append(last_morph.base)
                        joshiword_list.append("".join([m.surface for m in sentence[chunk_ind].morphs]))  # add

                if joshi_list != []:
                    # ソート後のインデックスをリスト化
                    sorted_index = sorted(range(len(joshi_list)), key=lambda k: joshi_list[k])  # add
                    sorted_joshi = " ".join(sorted(joshi_list))
                    sorted_joshiword = " ".join([joshiword_list[i] for i in sorted_index])  # add
                    f.write("{}\t{}\t{}\n".format(verb, sorted_joshi, sorted_joshiword))

f.close()
