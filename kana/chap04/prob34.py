#-*- coding: utf-8 -*-
#34. AのB

from prob30 import make_list

## 問題30で作ったリスト読み込み
all_list = make_list()

## 名詞　の(助詞) 名詞 となっていたら出力

meisiku = [] #3単語集めるリスト

for sentence_list in all_list:
	for mecab_dict in sentence_list:

		if len(meisiku) > 1: #2単語以上たまってから判定処理
		
			# 2つ前が名詞で、1つ前が「の」で現単語が名詞なら名詞句
			if (meisiku[0]['pos'] == "名詞") & (meisiku[1]['surface'] == "の")\
			& (meisiku[1]['pos'] == "助詞") & (mecab_dict['pos'] == "名詞"):
				print(meisiku[0]['surface'] + meisiku[1]['surface'] + mecab_dict['surface'])

			# 3単語たまってたら、1単語目を削除	
			if len(meisiku) > 2:
				meisiku.pop(0)

		# 今見ていた単語を加える
		meisiku.append(mecab_dict)	