#-*- coding: utf-8 -*-

import nlp40
import nlp41

if __name__=='__main__':
    with open("neko.txt.cabocha", "r", encoding="utf-8") as f:
        lines = f.readlines()
    lst = nlp41.make_chunk(lines)
    for l in lst:
        for ll in l:
            if ll.dst!='-1':
                flag = 0 # 名詞があるかどうか
                noun_lst = [] # 係り元
                for morph in ll.morphs:
                    if morph.pos=='名詞':
                        flag = 1
                    if morph.pos!='記号':
                        noun_lst.append(morph.surface)
                
                verb_lst = [] # 係り先
                for morph in l[int(ll.dst)].morphs:
                    if flag==1 and morph.pos=='動詞':
                        flag = 2

                    if morph.pos!='記号':
                        verb_lst.append(morph.surface)

                if flag==2:
                    for n in noun_lst:
                        print(n, end="")

                    print("\t", end="")

                    for v in verb_lst:
                        print(v, end="")

                    print("")
