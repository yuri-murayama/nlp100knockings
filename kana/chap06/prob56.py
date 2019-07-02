#-*- coding: utf-8 -*-
#56. 共参照解析

from xml.etree import ElementTree
import re

class Coreference:
	"""
	Coreference データ : sentence_id, token_id_start, token_id_start, representatice_mentionを要素としてもつ
	"""
	def __init__(self, sentence_id, token_id_start, token_id_end, representative_mention):
		self.sentence_id = int(sentence_id)
		self.token_id_start = int(token_id_start)
		self.token_id_end = int(token_id_end)
		self.representative_mention = representative_mention

# XMLファイルを解析
tree = ElementTree.parse('nlp.txt.new.xml')

# XMLを取得
root = tree.getroot()

# 参照表現を代表参照表現に置き換えるsentence_id, token_id開始位置, token_id終端位置, 代表参照表現本体　を保存
coreference_list = []	
for mention in root.iter("mention"):
	if mention.attrib.get("representative") != None:
		representative = mention.find("text").text
	else: # もし代表参照表現でなかったら，Coreferenceデータ型へ
		coreference = Coreference(mention.find("sentence").text, mention.find("start").text, mention.find("end").text, representative)
		coreference_list.append(coreference) #リストに保存

sentence_list = [] #sentenceごとにtokenのリストを作る
for sentence in root.iter('sentence'):
	word_list = []
	for token in sentence.iter('token'):
		word_list.append(token.find("word").text)
	if word_list != []:	
		sentence_list.append(word_list)	

sentence_id_list = [] #参照表現が出現したsentence_idを保存しておく
for c in coreference_list:
	c.token_id_start += sentence_id_list.count(c.sentence_id) #今まで代表参照表現を挿入したぶんだけ+
	c.token_id_end += sentence_id_list.count(c.sentence_id)
	sentence_id_list.append(c.sentence_id)
	word_list = sentence_list[c.sentence_id-1]
	word_list[c.token_id_end-2] = word_list[c.token_id_end-2] +")" + " 」"
	word_list.insert(c.token_id_start-1, "「 " + c.representative_mention + " (") #代表参照表現を挿入

for word_list in sentence_list: #出力用に綺麗に整える(''や', -LRB-, -RRB-)
	sentence = " ".join(word_list)
	sentence = re.sub(r'``\s', '"', sentence)
	sentence = re.sub(r'\s\'\'', '"', sentence)
	sentence = re.sub(r'\s\'', "'", sentence) 
	sentence = re.sub(r'`\s', "'", sentence) 
	sentence = re.sub(r'\s\,', ',', sentence)
	sentence = re.sub(r'\s\.', '.', sentence)
	sentence = re.sub(r'\(\s', '(', sentence)
	sentence = re.sub(r'-LRB-', '(', sentence)
	sentence = re.sub(r'-RRB-', ')', sentence)
	print(sentence)