#-*- coding: utf-8 -*-
#14.先頭からN行を表示

import sys

#指定行数N
N = int(sys.argv[1])

#ファイルの読み込み
with open('hightemp.txt', mode = 'r') as f:
	text = f.readlines()

if N > len(text):
	print("指定行数がファイルの行数を超えています")

else:
	for line in text[:N]:
		print(line, end = "")		