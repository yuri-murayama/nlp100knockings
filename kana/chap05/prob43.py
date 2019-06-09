#-*- coding: utf-8 -*-
#43. 名詞を含む文節が動詞を含む文節に係るものを抽出

from prob40 import Morph
from prob41 import Chunk
from prob41 import make_chunk_list

## 問題41で作ったリスト読み込み
all_list = make_chunk_list()

def print_morphs(morphs):

	for morph in morphs:
		if(morph.pos != "記号"):
			print(morph.surface, end = "")

## 1文ずつ見ていく
for sentence_list in all_list:
	for chunk in sentence_list:
		# 今の文節が名詞を含む文節か確認
		noun = False
		verb = False
		for morph in chunk.morphs:
			if morph.pos == "名詞":
				noun = True
				break;
		# 係先の文節が動詞を含む文節か確認
		if chunk.dst != -1: #文末でないこと確認
			for morph in sentence_list[chunk.dst].morphs:
				if morph.pos == "動詞":
					verb = True
					break;

		# 上をどっちも満たしてたら表示(記号除く)
		if noun == True & verb == True:
			# 係元の文節を表示
			print_morphs(chunk.morphs)
			# 係先の文節を表示
			print("\t", end = "")
			print_morphs(sentence_list[chunk.dst].morphs)
			print()

		