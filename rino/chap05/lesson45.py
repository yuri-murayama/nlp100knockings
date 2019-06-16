# -*- coding: utf-8 -*-

from lesson41 import getNekoChunk

OUTPUT_TXT = "./output45.txt"
f = open(OUTPUT_TXT, "w")

neko_chunk_list = getNekoChunk()

for sentence in neko_chunk_list:
    for a_chunk in sentence:
        for a_morph in a_chunk.morphs:

            if a_morph.pos == "動詞":
                verb = a_morph.base
                joshi_list = []

                for chunk_ind in a_chunk.srcs:
                    # morphの最後が助詞のため最後のみ取得
                    last_morph = sentence[chunk_ind].morphs[-1]
                    if last_morph.pos == "助詞":
                        joshi_list.append(last_morph.base)

                if joshi_list != []:
                    f.write("{}\t{}\n".format(verb, " ".join(sorted(joshi_list))))

f.close()

"""
========
出力結果
========

コーパス中で頻出する述語と格パターンの組み合わせ
> sort output45.txt | uniq

「する」の格パターン（「見る」「与える」も同様
> grep "^する\s" output45.txt | sort | uniq

"""
