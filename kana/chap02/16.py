#-*- coding: utf-8 -*-
#16.ファイルをN分割する

import sys
import numpy as np

#指定分割数N
N = int(sys.argv[1])

#ファイルの読み込み
with open('hightemp.txt', mode = 'r') as f:
	text = f.readlines()

if N > len(text):
	print("指定分割数がファイルの行数を超えています")	

else:
	text_split = list(np.array_split(text, N))

	for i, text_each in enumerate(text_split):
		with open(str(i) + '_hightemp.txt', mode = 'w') as f:
			f.writelines(list(text_each))

