#-*- coding: utf-8 -*-
#23.セクション構造

import re

	
# 問20で抽出したイギリスの記事のファイルを使用
with open("article.txt", mode = 'r') as f:
	for line in f:
		line = line.strip()
		#レベル3からマッチしていくか見ていく
		# ==タイトル== レベル1
		# ===タイトル===　レベル2
		# ====タイトル====　レベル3
		pattern1 = "=="
		pattern2 = "==="
		pattern3 = "===="
		if re.match(pattern3, line) != None:
			print("セクション名 : {}".format(re.sub(pattern3, '',line)), end = "")
			print("  レベル : 3")
		elif re.match(pattern2, line) != None:
			print("セクション名 : {}".format(re.sub(pattern2, '',line)), end = "")
			print("  レベル : 2")
		elif re.match(pattern1, line)!= None:
			print("セクション名 : {}".format(re.sub(pattern1, '',line)), end = "")
			print("  レベル : 1")