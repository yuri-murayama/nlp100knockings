#-*- coding: utf-8 -*-
import nlp40
import nlp41

def verb_mining(sentence):
    for chunk in sentence:
        morphs = chunk.morphs

        verb_lst = []
        for morph in morphs:
            if morph.pos == '動詞':
                verb_lst.append(morph.base) # 文節中の動詞を全て格納

        if len(verb_lst) > 0: # 動詞がある節に対して
                joshi_chunk_lst = chunk.srcs

                if len(joshi_chunk_lst) > 0: # 係り元がある
                    # サ変+をの抽出
                    sahen_wo = ''
                    for i in joshi_chunk_lst:
                        for j, m in enumerate(sentence[int(i)].morphs[:-1]):
                            if m.pos1 == 'サ変接続' and m.pos == '名詞':
                                if sentence[int(i)].morphs[j+1].pos == '助詞' and sentence[int(i)].morphs[j+1].surface == 'を':
                                    sahen_wo += m.surface + sentence[int(i)].morphs[j+1].surface
                                    joshi_chunk_lst.remove(i) # 述語に含むので係り元リストから削除

                    # 助詞の抽出
                    joshi_lst = []
                    joshi_part = [] # １つの説の中の助詞を考える
                    joshi_frame_lst = []
                    for i in joshi_chunk_lst:
                        for m in sentence[int(i)].morphs:
                            if m.pos == '助詞':
                                joshi_part.append(m.base)

                        # 助詞が含まれていた時
                        if len(joshi_part) > 0:
                            joshi_lst.append(joshi_part[-1]) # 最後の一つを助詞の代表とする

                        # 助詞を含むフレームを抽出
                        if len(joshi_lst) > 0:
                            joshi_frame = []
                            for mm in sentence[int(i)].morphs:
                                joshi_frame.append(mm.surface)
                            
                            joshi_frame_lst.append("".join(joshi_frame))
                    
                    if len(joshi_lst)>0 and len(sahen_wo)>0: # 格 and サ変+を がある
                        joshi = " ".join(joshi_lst)
                        joshi_frame = " ".join(joshi_frame_lst)

                        print(sahen_wo + verb_lst[0], end="")
                        print("\t", end="")
                        print(joshi, end="")
                        print("\t", end="")
                        print(joshi_frame)

if __name__=='__main__':
    with open("neko.txt.cabocha", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    lst = nlp41.make_chunk(lines)

    for sen in lst:
        verb_mining(sen)

"""
UNIX 確認コマンド
1.コーパス中で頻出する述語（サ変接続名詞+を+動詞）
cut -f 1 out47.txt | sort | uniq -c | sort -nr (| head -10)

2.コーパス中で頻出する述語と助詞パターン
cut -f 1,2 out47.txt | sort | uniq -c | sort -nr (| head -10)
"""