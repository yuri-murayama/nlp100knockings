#-*- coding: utf-8 -*-
import nlp40
import nlp41

def print_kaku_pattern(sentence):
    for chunk in sentence:
        morphs = chunk.morphs

        verb_lst = []
        for morph in morphs:
            if morph.pos == '動詞':
                verb_lst.append(morph.base)

        if len(verb_lst) > 0: # 動詞がある節に対して
        
            kaku_chunk_lst = chunk.srcs

            if len(kaku_chunk_lst)>0: # 係り元がある
                # 格の抽出
                kaku_lst = []
                for i in kaku_chunk_lst:
                    for m in sentence[int(i)].morphs:
                        if m.pos == '助詞':
                            kaku_lst.append(m.base)
                
                if len(kaku_lst)>0: # 格がある
                    kaku = " ".join(kaku_lst)
                    print(verb_lst[0], end="")
                    print("\t", end="")
                    print(kaku)

if __name__=='__main__':
    with open("neko.txt.cabocha", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    lst = nlp41.make_chunk(lines)

    for sen in lst:
        print_kaku_pattern(sen)

"""
UNIX 確認コマンド
1.コーパス中で頻出する述語と格パターンの組み合わせ
cut -f 1,2 out45.txt | sort | uniq -c | sort -nr (| head -10)

2.「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
grep "^する" out45.txt | sort | uniq -c | sort -nr | head -10
grep "^見る" out45.txt | sort | uniq -c | sort -nr | head -10
grep "^与える" out45.txt | sort | uniq -c | sort -nr | head -10
"""