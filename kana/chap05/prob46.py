#-*- coding: utf-8 -*-
#46.動詞の格フレーム情報の抽出


from prob41 import make_chunk_list

## 問題41で作ったリスト読み込み
all_list = make_chunk_list()


## 1文ずつ見ていく
for sentence_list in all_list:
	for chunk in sentence_list:
		pp_list = [] #助詞を保存しておくリスト
		verb = None #動詞を保存しておく変数
		chunk_list = [] #助詞を含む文節を保存しておくリスト

		# 今の文節が動詞を含む文節か確認
		for morph in chunk.morphs:
			if morph.pos == "動詞":
				verb = morph.base
				break;

		# 係元に助詞があるかを確認
		if verb != None:
			for src in chunk.srcs:
				pos_list = [morph.pos for morph in sentence_list[src].morphs]
				if "助詞" in pos_list:
					# 助詞を含む形態素番号取得
					pos_indexes = [i for i, pos_index in enumerate(pos_list) if pos_index == "助詞"]
					# 最後の助詞だけとる
					pos_index = pos_indexes[-1]
					# その文節ごと変数に保存
					chunk_src = [morph.surface for morph in sentence_list[src].morphs if morph.pos != "記号"]
					chunk_src = "".join(chunk_src)
					# リストに保存していく
					pp_list.append(sentence_list[src].morphs[pos_index].base)
					chunk_list.append(chunk_src)

		# 助詞 + 動詞　の組み合わせだったら
		if (verb != None) & (pp_list != []):
			pp_list = " ".join(pp_list)
			chunk_list = " ".join(chunk_list)
			print(verb, end = "\t")
			print("\t", end = "")
			print(pp_list, end = "\t")
			print("\t", end = "")
			print(chunk_list)