#-*- coding: utf-8 -*-
#18.各行を3コラム目の数値の降順にソート

import numpy as np

# ファイルを読み込み、3列目のみ取り出してリストにしておく
list_3 = []
text_list = []
with open('hightemp.txt', mode = 'r') as f:
	# 1行読み込んでtab区切りでリストへ
	for text in f:
		text_list.append(text)
		word_list = text.split('\t')
		list_3.append(word_list[2])

# 3列目で逆順ソートした時のindexを取り出しておく
sorted_index = np.argsort(list_3)[::-1]

# 求めたindexでテキスト全体をソート
text_list = np.array(text_list)[sorted_index]

#ファイルに書き込み
with open('hightemp_reverse.txt', mode = 'w') as f:
	f.writelines(text_list)