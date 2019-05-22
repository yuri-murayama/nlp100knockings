#-*- coding: utf-8 -*-
#38.Zipfの法則

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

##順位のリストを作る
rank_list = [] 
rank = 1 # 順位を表す変数 初期値1
rank_range = 0 # 同じ順位の個数を表す変数 初期値0
preb_count = max(count_list) # 1つ前の単語の頻度を表す 初期値は1位の頻度
for count in count_list:
	# 1つ前の単語の頻度より少なくなってたら
	if count != preb_count:
		rank += rank_range # 順位は1つ前の同一順位の個数分下がる
		preb_count = count # preb_count更新
		rank_range = 1 # rank_rangeリセット
		rank_list.append(rank) # 順位保存
	# 1つ前の単語の頻度と同じだったら	
	else:
		rank_range += 1 # rank_range 1増える
		rank_list.append(rank) # 順位保存

## 両対数表示
plt.plot(rank_list, count_list)
plt.xscale('log')
plt.yscale('log')
plt.title("問39.Zipfの法則")
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.show()
plt.savefig('./plot/plot_39.png')