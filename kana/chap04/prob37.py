#-*- coding: utf-8 -*-
#37.頻度上位10語

from prob30 import make_list
from prob36 import get_vocab_count
import matplotlib.pyplot as plt
import matplotlib as mpl

## フォントを指定する。
mpl.rcParams["font.family"] = "AppleGothic"

## 問題30で作ったリスト読み込み
all_list = make_list()

## 問題36で作った単語頻度順のリスト読み込み
sorted_vocab_count = get_vocab_count(all_list)

##上位10単語について、単語のリストとカウントのリストを作る
vocab_list = [word for (word, count) in sorted_vocab_count[:10]]
count_list = [count for  (word, count) in sorted_vocab_count[:10]]

## 棒グラフでプロット
plt.bar(vocab_list, count_list)
plt.title("問37.頻度上位10語")
plt.xlabel('出現頻度が高い10語')
plt.ylabel('出現頻度')
plt.show()
plt.savefig('./plot/plot_37.png')
