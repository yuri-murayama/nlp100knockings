#-*- coding: utf-8 -*-
import nlp40
import nlp41

def print_kaku_frame(sentence):
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
                kaku_frame_lst = []
                for i in kaku_chunk_lst:
                    for m in sentence[int(i)].morphs:
                        if m.pos1 == '格助詞':
                            kaku_lst.append(m.base)

                            kaku_frame = []
                            for mm in sentence[int(i)].morphs:
                                if mm.pos1!='句点':
                                    kaku_frame.append(mm.surface)
                            
                            kaku_frame_lst.append("".join(kaku_frame))
                
                if len(kaku_lst)>0: # 格がある
                    kaku = " ".join(kaku_lst)
                    kaku_frame = " ".join(kaku_frame_lst)

                    print(verb_lst[0], end="")
                    print("\t", end="")
                    print(kaku, end="")
                    print("\t", end="")
                    print(kaku_frame)

if __name__=='__main__':
    with open("neko.txt.cabocha", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    lst = nlp41.make_chunk(lines)

    for sen in lst:
        print_kaku_frame(sen)
