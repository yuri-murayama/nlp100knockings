#-*- coding: utf-8 -*-
#38.ヒストグラム

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

##上位10単語について、カウントのリストを作る
count_list = [count for  (word, count) in sorted_vocab_count]

## ヒストグラムでプロット(1000回以上のみ)
plt.hist(count_list, bins = 20, range = (1000,9000), rwidth = 0.8)
plt.title("問38.ヒストグラム")
plt.xlabel('出現頻度')
plt.ylabel('出現頻度をとる単語の種類数')
plt.savefig('./plot/plot_38.png')
plt.show()
