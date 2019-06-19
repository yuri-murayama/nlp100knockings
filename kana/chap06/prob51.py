#-*- coding: utf-8 -*-
#51. 単語の切り出し

# prob50で作ったファイルを読み込む
with open("output50.txt", mode = 'r') as f:
	for line in f:
		line = line.strip() #改行除去
		line = line.split(' ') #スペース区切りで単語リストへ
		print('\n'.join(line))
		print() #文末に改行を入れる