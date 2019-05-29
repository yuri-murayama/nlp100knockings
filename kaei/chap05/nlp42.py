#-*- coding: utf-8 -*-

import nlp40
import nlp41

if __name__=='__main__':
    lst = nlp41.make_chunk()
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
