# -*- coding: utf-8 -*-

from lesson41 import getNekoChunk

OUTPUT_TXT = "./output47.txt"
f = open(OUTPUT_TXT, "w")

neko_chunk_list = getNekoChunk()

for sentence in neko_chunk_list:
    for a_chunk in sentence:
        is_use_flag = 0  # 動詞のヲ格にサ変名詞が入っているかのフラグ

        for a_morph in a_chunk.morphs:
            if a_morph.pos == "動詞":
                joshi_list = []
                joshiword_list = []

                for chunk_ind in a_chunk.srcs:
                    # morphの最後が助詞のため最後のみ取得
                    num = -1
                    last_morph = sentence[chunk_ind].morphs[num]

                    # 、が入ってしまう場合はその1つ前が助詞かどうかチェックする
                    if last_morph.surface == "、":
                        num -= 1
                        last_morph = sentence[chunk_ind].morphs[num]

                    if ((last_morph.pos == "助詞" and last_morph.surface == "を")
                        and sentence[chunk_ind].morphs[num-1].pos1 == "サ変接続"):
                        # 「サ変接続名詞+を(助詞)」となっているか？
                        is_use_flag = 1
                        verb = sentence[chunk_ind].morphs[num-1].surface + "を" + a_morph.base

                    elif last_morph.pos == "助詞":
                        # ヲ格以外の述語にかかる助詞をアペンド
                        joshi_list.append(last_morph.base)
                        joshiword_list.append("".join([m.surface for m in sentence[chunk_ind].morphs]))

        if is_use_flag == 1:
            # ソート後のインデックスをリスト化
            sorted_index = sorted(range(len(joshi_list)), key=lambda k: joshi_list[k])
            sorted_joshi = " ".join(sorted(joshi_list))
            sorted_joshiword = " ".join([joshiword_list[i] for i in sorted_index])
            f.write("{}\t{}\t{}\n".format(verb, sorted_joshi, sorted_joshiword))

f.close()

"""
========
出力結果
========
# TODO: "、"が入ってしまうのを消す
返事をする	と に は	及ばんさと、 手紙に 主人は


コーパス中で頻出する述語（サ変接続名詞+を+動詞）
> cut -f 1 output47.txt | sort | uniq -c | sort -r
27 返事をする
19 挨拶をする
14 真似をする
12 喧嘩をする
10 話をする

コーパス中で頻出する述語と助詞パターン
> cut -f 1,2 output47.txt | sort | uniq -c | sort -r
8 真似をする
6 返事をする	と
6 運動をする
6 喧嘩をする
4 返事をする	と は
4 挨拶をする	と

"""
