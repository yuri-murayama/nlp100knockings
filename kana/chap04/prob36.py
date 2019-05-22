#-*- coding: utf-8 -*-
#36.単語の出現頻度

from prob30 import make_list

## 単語の頻度を数えてソートする関数
def get_vocab_count(all_list):

	vocab_count = {} #単語の出現頻度の辞書 key:単語 value:数

	for sentence_list in all_list:
		for mecab_dict in sentence_list:
			#原形を取り出す
			word = mecab_dict['base']
			#すでに辞書にあったら
			if word in vocab_count.keys():
				vocab_count[word] += 1
			#なかったら	
			else:
				vocab_count[word] = 1

	#頻度順にソート
	sorted_vocab_count = sorted(vocab_count.items(), key=lambda x: -x[1])

	return(sorted_vocab_count)		

if __name__ == '__main__':
	## 問題30で作ったリスト読み込み
	all_list = make_list()
	#実行
	print(get_vocab_count(all_list))