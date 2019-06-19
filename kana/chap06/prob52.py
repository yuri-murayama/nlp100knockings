#-*- coding: utf-8 -*-
#52.ステミング

from nltk.stem.porter import PorterStemmer as PS

# prob51で作ったファイルを読み込む
with open('output51.txt', mode = 'r') as f:
	ps = PS()
	for line in f:
		line = line.strip() #改行除去
		print(line, end = "\t") #単語を出力
		print(ps.stem(line)) #語幹を出力