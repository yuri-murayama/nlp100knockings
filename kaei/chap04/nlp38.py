#-*- coding: utf-8 -*-

import nlp30
import nlp36

import matplotlib.pyplot as plt

def appear(dic):
    count_dic = {}
    for k, v in dic:
        if v in count_dic:
            count_dic[v] +=1
        else:
            count_dic[v] = 1
    return count_dic

if __name__=='__main__':
    lst = nlp30.make_lst()
    dic = nlp36.count_word(lst)
    dic = sorted(dic.items(), key=lambda x: -x[1])
    count_dic = appear(dic)

    y = []
    label = []
    for k, v in count_dic.items():
        y.append(v)
        label.append(k)
        

    plt.rcParams['font.family'] = 'AppleGothic'
    plt.hist(y, bins=len(label), label=label)
    plt.show()
