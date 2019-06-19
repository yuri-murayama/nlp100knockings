#-*- coding: utf-8 -*-
#50. 文区切り

import re

#ファイルの読み込み
split_text = []
with open("nlp.txt", mode = 'r') as f:
	for line in f:
		#line = re.sub(r'\n', '', line) #改行除去
		line = line.strip() #改行除去
		if line == '': #1行空きだったら処理を飛ばす
			continue
		pattern = r'(\.|;|:|\?|!)\s[A-Z]' #パターン(. or ; or : or ? or !) → 空白文字 → 英大文字
		match = re.search(pattern, line)
		while match != None: #パターンが見つからなくなるまで文に区切る
			split_text.append(line[:match.start()+1]) #記号までを1行として保存
			line = line[match.end()-1:] #先頭になっている大文字から次にみる文章とする
			match = re.search(pattern, line) #パターンを見つける
		split_text.append(line) #最後見つからなかったら、ここに保存

for sentence in split_text:
	print(sentence)