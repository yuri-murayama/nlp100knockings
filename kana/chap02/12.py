#-*- coding: utf-8 -*-
#12.1列目をcol1.txtに，2列目をcol2.txtに保存

# ファイルを読み込んで、1列目と2列目を別々の配列に
list_1 = []
list_2 = []
with open('hightemp.txt', mode = 'r') as f:
	#1行読み込んでtab区切りでリストへ
	for text in f:
		word_list = text.split('\t')
		list_1.append(word_list[0])
		list_2.append(word_list[1])

# 1列目をcol1.txtに，2列目をcol2.txtに保存
with open('col1.txt', mode = 'w') as f:
	# list_1を1行ごとに出力
	f.writelines('\n'.join(list_1))

with open('col2.txt', mode = 'w') as f:
	# list_2を1行ごとに出力
	f.writelines('\n'.join(list_2))