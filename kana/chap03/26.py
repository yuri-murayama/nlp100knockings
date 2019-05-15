#-*- coding: utf-8 -*-
#26.強調マークアップの除去

import re

def remove(text):

	#''か'''か'''''を除去
	text = re.sub(r'\'{3}|\'{5}|\"', '', text)
	
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

# 辞書にして表示(強調マークアップ除去)
d = {field[0]:remove(field[1]) for field in field_list}

for k, v in d.items():
    print('{0} : {1}'.format(k,v)) 		

