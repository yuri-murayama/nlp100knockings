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
                for morph in ll.morphs:
                    if morph.pos!='記号':
                        print(morph.surface, end="")
                print("\t", end="")
                for morph in l[int(ll.dst)].morphs:
                    if morph.pos!='記号':
                        print(morph.surface, end="")
                print("")
