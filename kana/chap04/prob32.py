#-*- coding: utf-8 -*-
#31. 動詞の原形

from prob30 import make_list

#問題30で作ったリスト読み込み
all_list = make_list()

for sentence_list in all_list:
	for mecab_dict in sentence_list:
		# 動詞だったら
		if mecab_dict['pos'] == "動詞":
			# 原形を表示
			print(mecab_dict['base'])