#-*- coding: utf-8 -*-
#33. サ変名詞

from prob30 import make_list

#問題30で作ったリスト読み込み
all_list = make_list()

for sentence_list in all_list:
	for mecab_dict in sentence_list:
		# サ変接続の名詞だったら
		if (mecab_dict['pos'] == "名詞") & (mecab_dict['pos1'] == "サ変接続") :
			# 表層系を表示
			print(mecab_dict['surface'])