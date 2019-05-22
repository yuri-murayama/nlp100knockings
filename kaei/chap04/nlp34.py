#-*- coding: utf-8 -*-

import nlp30

def a_no_b(lst):
    for l in lst: # 1文
        for i, ll in enumerate(l): # 1語
            if i+2 < len(l):
                if ll['pos'] == "名詞":
                    if l[i+1]['pos'] == "助詞" and l[i+1]['surface'] == "の":
                        if l[i+2]['pos'] == "名詞":
                            print(ll["surface"]+l[i+1]["surface"]+l[i+2]["surface"])
                


if __name__=='__main__':
    lst = nlp30.make_lst()
    a_no_b(lst)
