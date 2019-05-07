#-*- coding: utf-8 -*-
#17.１列目の文字列の異なり

# ファイルを読み込み、1列目のみ取り出す
list_1 = []
with open('hightemp.txt', mode = 'r') as f:
	#1行読み込んでtab区切りでリストへ
	for text in f:
		word_list = text.split('\t')
		list_1.append(word_list[0])

print(set(list_1))		