#-*- coding: utf-8 -*-
#35. 名詞の連接(間違えちゃったバージョン:最長接続の最長を持ってきてしまった...)

from prob30 import make_list

## 問題30で作ったリスト読み込み
all_list = make_list()

## 名詞の連続を最長一致で出力(名詞が連なってる中で一番長いやつ)

noun_connect_max = [([], 0)] #最長の名詞の連続とその数をタプルとして保存しておくリスト

for sentence_list in all_list:

	noun_connect = [] #連続した名詞
	noun_connect_num = 0 #連続した名詞の数

	for mecab_dict in sentence_list:
		# 名詞だったらリストに保存して、連続個数をカウント
		if mecab_dict['pos'] == "名詞":
			noun_connect.append(mecab_dict['surface'])
			noun_connect_num += 1
		#名詞じゃなかったら
		else:
			# 今までの最長記録と比較
			if noun_connect_num > noun_connect_max[0][1]: #最大値を超えたら更新
				noun_connect_max = [(noun_connect, noun_connect_num)]
			elif noun_connect_num == noun_connect_max[0][1]: #最大値と同じだったらリストに加える
				noun_connect_max.append((noun_connect, noun_connect_num))
			# 名詞リストも連続個数もリセット	
			noun_connect = []
			noun_connect_num = 0

for connect in noun_connect_max:
	print(connect[0])


