#-*- coding: utf-8 -*-
import nlp50

def cut_word(sen_lst):
    word_lst = []
    for sen in sen_lst:
        sen = sen.replace(',', '')
        sen = sen.replace('.', '')
        words = sen.split(' ')
        word_lst.append(words)
    
    return word_lst

if __name__=='__main__':
    with open("nlp.txt") as f:
        lines = f.readlines() # 改行あり
    
    sen_lst = nlp50.make_senlst(lines)
    word_lst = cut_word(sen_lst)

    for words in word_lst:
        print("\n".join(words))
        print()