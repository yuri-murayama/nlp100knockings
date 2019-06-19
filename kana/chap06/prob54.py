#-*- coding: utf-8 -*-
#54. 品詞タグ付け

import re

# 作ったnlp.txt.xmlを読み込んで単語，レンマ，品詞をタブ区切り形式で出力
with open("nlp.txt.xml", mode = 'r') as f:
	for line in f:

		pattern = r'<word>(.*?)</word>' #単語のパターン生成
		match = re.search(pattern, line) #検索
		if match != None:
			print(re.sub(r'<word>|</word>', '', match.group()), end = "\t") #<word></word>で囲まれた部分出力
		
		pattern = r'<lemma>(.*?)</lemma>' #レンマのパターン生成
		match = re.search(pattern, line) #検索
		if match != None:
			print(re.sub(r'<lemma>|</lemma>', '', match.group()), end = "\t") #<lemma></lemma>で囲まれた部分出力


		pattern = r'<POS>(.*?)</POS>' #品詞のパターン生成
		match = re.search(pattern, line) #検索
		if match != None:
			print(re.sub(r'<POS>|</POS>', '', match.group())) #<POS></POS>で囲まれた部分出力	