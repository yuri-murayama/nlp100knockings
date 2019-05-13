#-*- coding: utf-8 -*-
#21. カテゴリ名を含む行を抽出

if __name__ == '__main__':

	# 問20で抽出したイギリスの記事のファイルを使用
	with open("article.txt", mode = 'r') as f:
		for line in f:
			line = line.strip()
			# Categoryが含まれていたら、出力
			if "Category" in line:
				print (line)
