#-*- coding: utf-8 -*-
#35. 名詞の連接

from prob30 import make_list

## 問題30で作ったリスト読み込み
all_list = make_list()

## 名詞の連続を最長一致で出力(名詞が連なってる中で一番長いやつ)

for sentence_list in all_list:

	noun_connect = [] #連続した名詞

	for mecab_dict in sentence_list:
		# 名詞だったらリストに保存して、連続個数をカウント
		if mecab_dict['pos'] == "名詞":
			noun_connect.append(mecab_dict['surface'])
		# 連続名詞の後の単語だったら
		elif len(noun_connect) != 0:
			# 今までの連続した名詞を出力
			print(''.join(noun_connect))
			# 名詞リストリセット	
			noun_connect = []
			