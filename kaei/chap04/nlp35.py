#-*- coding: utf-8 -*-

import nlp30

def noun_noun(lst):
    result = ""
    flag = 0
    count = 0

    for l in lst: # 1文
        for ll in l: # 1語
            if flag == 0:
                if ll['pos'] == "名詞":
                    flag = 1
                    result = result + ll['surface']
                    count+=1

            elif flag == 1:
                if ll['pos'] == "名詞":
                    result = result + ll['surface']
                    count+=1

                else:
                    flag = 0
                    if count>1:
                        print(result)
                    result = ""
                    count = 0

if __name__=='__main__':
    lst = nlp30.make_lst()
    noun_noun(lst)
