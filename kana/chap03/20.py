#-*- coding: utf-8 -*-
#20.JSONデータの読み込み

import json


def extract_article(filename, country):

	target_article =[]

	with open(filename) as f:
		for line in f:
			article = json.loads(line)
			# titleがcontryになっているものだけ取り出す
			if article['title'] == country:
				target_article.append(article['text'])

	return target_article			

if __name__ == '__main__':

	# イギリスについての記事だけ取り出し
	filename = "jawiki-country.json"
	target_article = extract_article(filename, "イギリス")

	# textファイルに記事を出力
	with open('article.txt', mode = 'w') as f:
		f.writelines(target_article)