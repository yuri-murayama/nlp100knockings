#-*- coding: utf-8 -*-

import nlp30
import nlp36

import matplotlib.pyplot as plt

if __name__=='__main__':
    lst = nlp30.make_lst()
    dic = nlp36.count_word(lst)
    dic = sorted(dic.items(), key=lambda x: -x[1])

    label = []
    x = []
    y = []
    i = 0

    for k, v in dic:
        label.append(k)
        x.append(i)
        y.append(int(v))
        i+=1
        if i>9:
            break

    plt.rcParams['font.family'] = 'AppleGothic'
    plt.bar(x, y, tick_label=label, align='center')
    plt.show()
