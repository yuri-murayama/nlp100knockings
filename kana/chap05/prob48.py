#-*- coding: utf-8 -*-
#48.名詞から根へのパスの抽出

from prob41 import make_chunk_list

## 問題41で作ったリスト読み込み
all_list = make_chunk_list()

def print_pass(sentence_list, chunk):

	# 文節を出力
	print(" -> ", end = "")
	chunk_surface = [morph.surface for morph in chunk.morphs if morph.pos != "記号"]
	print("".join(chunk_surface), end = "")

	# 次が文末だったら終了
	if chunk.dst != -1:
		return print_pass(sentence_list, sentence_list[chunk.dst])
	else:
		return 0	

## 1文ずつ見ていく
for sentence_list in all_list:
	for chunk in sentence_list:

		# 今の文節が名詞を含む文節か確認
		pos_list = [morph.pos for morph in chunk.morphs]
		if "名詞" in pos_list:
			# 名詞を含む文節を出力
			chunk_surface = [morph.surface for morph in chunk.morphs if morph.pos != "記号"]
			print("".join(chunk_surface), end = "")
			# 係先を出力していく
			print_pass(sentence_list, sentence_list[chunk.dst])
			print()
				
				
		