#-*- coding: utf-8 -*-
#53. Tokenization

import re

# 作ったnlp.txt.xmlを読み込んで1行1単語で出力
with open("nlp.txt.xml", mode = 'r') as f:
	for line in f:
		pattern = r'<word>(.*?)</word>' #パターン生成
		match = re.search(pattern, line) #検索
		if match != None:
			print(re.sub(r'<word>|</word>', '', match.group())) #<word></word>で囲まれた部分出力
