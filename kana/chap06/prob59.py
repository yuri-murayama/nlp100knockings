#-*- coding: utf-8 -*-
#59. S式の解析

from xml.etree import ElementTree
import re

# XMLファイルを解析
tree = ElementTree.parse('nlp.txt.new.xml')
# XMLを取得
root = tree.getroot()

def check_brackets(expr):
	"""
	最初の開き括弧と一致する閉じる括弧が見つかったらそこまでのexprを返す
	(NP以降のS式全体を受け取ってきて、NPの部分の文字列を返す)
	"""	
	stack = 0
	for i, c in enumerate(expr):
		if c == "(":
			stack += 1
		elif c == ")":
			stack -= 1
		
		if stack == 0:
			return expr[:i+1] 

	return 1 #異常終了
	
		
for parse in root.iter("parse"):
	sentence = parse.text
	pattern = r"\(NP"
	
	match = re.search(pattern, sentence) #(NPから始まる部分文字列を獲得
	while match != None: 
		np = check_brackets(sentence[match.start():]) #括弧が閉じるまで取り出す
		print(re.sub(r"(\(\S+?\s)|(\))", r"", np))
		sentence = sentence[match.end():] #次の(NPから始まる部分文字列を獲得
		match = re.search(pattern, sentence)
	print()	