#-*- coding: utf-8 -*-
#27.内部リンクの除去

import re

def remove(text):

	#強調マークアップ除去：''か'''か'''''を除去
	text = re.sub(r'\'{3}|\'{5}|\"', '', text)

	#内部リンク除去 [[記事名|表示文字]] を 表示文字 にする Ver.
	text = re.sub(r'(.*?)\[\[.*?\|([^|]*?)\]\](.*?)', '\\1\\2\\3', text)

	#内部リンク除去 [[表示文字]] を　表示文字 にする Ver.
	text = re.sub(r'(.*?)\[\[(.*?)\]\](.*?)', '\\1\\2\\3', text)

	return text 

#ファイルの読み込み
with open("article.txt", mode = 'r') as f:
	text = ''.join(f)

#基礎情報のパターン作成
pattern = r'基礎情報.*?^(.*?)^\}\}'
[base_info] = re.findall(pattern, text, flags = re.MULTILINE|re.DOTALL)

#フィールド名と値のパターン作成
pattern = r'^\|(.*?)\s\=\s(.*?)$'
field_list = re.findall(pattern, base_info, flags = re.MULTILINE)

# 辞書にして表示(強調マークアップ、内部リンク除去)
d = {field[0]:remove(field[1]) for field in field_list}

for k, v in d.items():
    print('{0} : {1}'.format(k,v)) 
