#-*- coding: utf-8 -*-

import nlp30

def count_word(lst):
    dic = {}

    for l in lst: # 1文
        for ll in l: # 1語
            if ll['base'] in dic:
                dic[ll['base']] += 1
            else:
                dic[ll['base']] = 1

    return dic

if __name__=='__main__':
    lst = nlp30.make_lst()
    dic = count_word(lst)
    for k, v in sorted(dic.items(), key=lambda x: -x[1]):
        print(k, ':', v)
