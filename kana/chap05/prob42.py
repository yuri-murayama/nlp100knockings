#-*- coding: utf-8 -*-
#42. 係り元と係り先の文節の表示

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
		# 今の文節を表示(句読点などの記号除く)
		print_morphs(chunk.morphs)
		# 係先の文節を表示
		print("\t", end = "")
		if chunk.dst != -1:
			print_morphs(sentence_list[chunk.dst].morphs)
		else:
			print("文末")	
		print()
