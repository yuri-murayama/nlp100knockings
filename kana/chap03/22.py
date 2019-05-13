#-*- coding: utf-8 -*-
#22. カテゴリ名の抽出

import re


# 問20で抽出したイギリスの記事のファイルを使用
with open("article.txt", mode = 'r') as f:
	for line in f:
		line = line.strip()
		# Categoryが含まれている行のみについて
		if "Category" in line:
			pattern = r'[!-/:-@[-`{-~]|[a-zA-Z]'
			print(re.sub(re.compile(pattern), '', line))