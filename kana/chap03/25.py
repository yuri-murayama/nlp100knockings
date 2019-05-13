#-*- coding: utf-8 -*-
#25.テンプレートの抽出

import re

#ファイルの読み込み
with open("article.txt", mode = 'r') as f:
	text = ''.join(f)

#基礎情報のパターン作成
pattern = r'基礎情報.*?^(.*?)^\}\}'
[base_info] = re.findall(pattern, text, flags = re.MULTILINE|re.DOTALL)

#フィールド名と値のパターン作成
pattern = r'^\|(.*?)\s\=\s(.*?)$'
field_list = re.findall(pattern, base_info, flags = re.MULTILINE)

# 辞書にして表示
d = {field[0]:field[1] for field in field_list}
print(d)
				
				