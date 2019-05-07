#-*- coding: utf-8 -*-
#15.末尾のN行を出力

import sys

#指定行数N
N = int(sys.argv[1])

#ファイルの読み込み
with open('hightemp.txt', mode = 'r') as f:
	text = f.readlines()

if N > len(text):
	print("指定行数がファイルの行数を超えています")

else:
	text = text[-N:]
	for line in text:
		print(line, end = "")		