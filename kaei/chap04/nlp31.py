#-*- coding: utf-8 -*-

import nlp30

def verb_surface(lst):
    for l in lst: # 1文
        for ll in l: # 1語
            if ll['pos'] == "動詞":
                print(ll['surface'])

if __name__=='__main__':
    lst = nlp30.make_lst()
    verb_surface(lst)
