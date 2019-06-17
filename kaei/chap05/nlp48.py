#-*- coding: utf-8 -*-
import nlp40
import nlp41

def noun_to_root(sentence):
    for i, chunk in enumerate(sentence):
        noun_frame = [] # 文節の単語を格納
        noun_lst = [] # 文節中の名詞を格納

        morphs = chunk.morphs

        for morph in morphs:
            if morph.pos == '名詞':
                noun_lst.append(morph.surface)

        if len(noun_lst) > 0:
            for m in sentence[int(i)].morphs:
                if m.pos1!='句点':
                    noun_frame.append(m.surface)

            print("".join(noun_frame), end="")

            dst = chunk.dst
            while dst!='-1':
                print(" -> ", end="")

                dst_frame = []
                for mm in sentence[int(dst)].morphs:
                    if mm.pos1!='句点':
                        dst_frame.append(mm.surface)
                print("".join(dst_frame), end="")
                dst = sentence[int(dst)].dst
            print()
    print()

if __name__=='__main__':
    with open("neko.txt.cabocha", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    lst = nlp41.make_chunk(lines)

    for sen in lst:
        noun_to_root(sen)