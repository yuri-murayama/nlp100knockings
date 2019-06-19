#-*- coding: utf-8 -*-
from stemming.porter2 import stem

import nlp50
import nlp51

def stemming(word_lst):
    for words in word_lst:
        for w in words:
            print(w, end="")
            print('\t', end="")
            print(stem(w))
        print()

if __name__=='__main__':
    with open("nlp.txt") as f:
        lines = f.readlines() # 改行あり
    
    sen_lst = nlp50.make_senlst(lines)
    word_lst = nlp51.cut_word(sen_lst)
    stemming(word_lst)