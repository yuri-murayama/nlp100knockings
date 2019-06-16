# -*- coding: utf-8 -*-

from lesson41 import getNekoChunk

def convertXY(c, xy):
    # chunkオブジェクトを受け取って、名詞をXorYに変換する関数
    text=""
    p_flag = 0
    x_pos = [m.pos for m in c.morphs]
    for p_i, p in enumerate(x_pos):
        if p == "名詞":
            if p_flag == 0:
                text += "{}".format(xy)
                p_flag = 1
            else:
                pass
        else:
            text += c.morphs[p_i].surface

    return text

OUTPUT_TXT = "./output49.txt"
f = open(OUTPUT_TXT, "w")

neko_chunk_list = getNekoChunk()

for sentence in neko_chunk_list:
    noun_ind_list = []  # 名詞を含む文節のインデックスを保存するリスト
    chunk_dict = {}   # {0:[1,2,-1], 1:[2,-1]}
    for ind, a_chunk in enumerate(sentence):

        # 名詞を含む文節のインデックスを取得
        if "名詞" in [m.pos for m in a_chunk.morphs]:
            noun_ind_list.append(ind)
            chunk_dict[ind] = []

            dst = a_chunk.dst
            chunk_dict[ind].append(dst)

            while 1:

                if dst == -1:
                    break

                dst = sentence[dst].dst
                chunk_dict[ind].append(dst)

    # 出力
    for i, i_ind in enumerate(noun_ind_list):
        for j, j_ind in enumerate(noun_ind_list[i+1:], i+1):

            text = ""

            ik_chunk_dst_list = [i_ind] + chunk_dict[i_ind]
            jk_chunk_dst_list = [j_ind] + chunk_dict[j_ind]

            # 文節iから文節kに至る直前のパスのインデックスのリスト
            ik_ind_list = []
            for ii in ik_chunk_dst_list:
                if ii in jk_chunk_dst_list:
                    break
                ik_ind_list.append(ii)

            # 文節jから文節kに至る直前のパスのインデックスのリスト
            jk_ind_list = []
            for jj in jk_chunk_dst_list:
                if jj in ik_chunk_dst_list:
                    break

                jk_ind_list.append(jj)

            # 文節kのインデックスのリスト
            k_ind_list = []
            for ii in ik_chunk_dst_list:
                if ii in jk_chunk_dst_list:
                    k_ind_list.append(ii)

            # 文節iから文節kの表示
            for num, ik in enumerate(ik_ind_list):
                if ik == i_ind:
                    text += convertXY(sentence[ik], "X")

                else:
                    text += "".join([m.surface for m in sentence[ik].morphs])

                if num != len(ik_ind_list)-1:
                    text += " -> "

            # 文節jから文節kの表示
            if jk_ind_list != []:
                text += " | "

                for num, jk in enumerate(jk_ind_list):
                    if jk == j_ind:
                        text += convertXY(sentence[jk], "Y")

                    else:
                        text += "".join([m.surface for m in sentence[jk].morphs])

                    if num != len(jk_ind_list)-1:
                        text += " -> "

                text += " | "

            else:
                text += " -> "

            # 文節kの表示
            for num, k in enumerate(k_ind_list):
                if k == -1:
                    break

                if k == j_ind:
                    text += "Y"
                    #print(convertXY(sentence[k], "Y"), end="")
                    break

                else:
                    text += "".join([m.surface for m in sentence[k].morphs])

                if num != len(k_ind_list)-2:
                    text += " -> "

            text += "\n"
            f.write(text)

f.close()

"""
========
出力結果
========
Xは | Yで -> 始めて -> 人間という -> ものを | 見た。
Xは | Yという -> ものを | 見た。
Xは | Yを | 見た。
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y

"""
