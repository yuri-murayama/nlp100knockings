#-*- coding: utf-8 -*-
#24.ファイル参照の抽出

import re

# 問20で抽出したイギリスの記事のファイルを使用
with open("article.txt", mode = 'r') as f:
	text = ''.join(f)
#ファイル：またはFile:となっている右側を取り出す
pattern = r"(?:ファイル|File):(.*?)\|"
a = re.findall(pattern, text)
print(a)	