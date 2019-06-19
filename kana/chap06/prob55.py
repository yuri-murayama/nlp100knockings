#-*- coding: utf-8 -*-
#55. 固有表現抽出

import re

# 作ったnlp.txt.xmlを読み込んで人名を表していたら、その単語を出力
# 人名のタグ:<NER>PERSON</NER>
with open("nlp.txt.xml", mode = 'r') as f:
	for line in f:

		pattern = r'<word>(.*?)</word>' #単語のパターン生成
		match = re.search(pattern, line) #検索
		if match != None:
			word = re.sub(r'<word>|</word>', '', match.group()) #<word></word>で囲まれた部分を単語として保存

		pattern = r'<NER>(.*?)</NER>' #単語のパターン生成
		match = re.search(pattern, line) #検索
		if match != None:
			if re.sub(r'<NER>|</NER>', '', match.group()) == "PERSON":
				print(word)