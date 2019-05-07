#-*- coding: utf-8 -*-
#18.各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

# ファイルを読み込み、1列目のみ取り出して都道府県と回数の辞書にしておく
dict_1 = {}
with open('hightemp.txt', mode = 'r') as f:
	# 1行読み込んでtab区切りでリストへ
	for text in f:
		word_list = text.split('\t')
		if word_list[0] in dict_1.keys():
			dict_1[word_list[0]] += 1
		else:
			dict_1[word_list[0]] = 1

# dict_1をvalue順にソートして、keyを出力
for k, v in sorted(dict_1.items(), key=lambda x: -x[1]):
    print(str(k) + ": " + str(v))
