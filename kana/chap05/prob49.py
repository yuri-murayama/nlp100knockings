#-*- coding: utf-8 -*-
#49.名詞間の係り受けパスの抽出

from prob41 import make_chunk_list

## 問題41で作ったリスト読み込み
all_list = make_chunk_list()

def make_pair_pass(sentence_list, chunk1, chunk2, chunk_pass_list, rep1, rep2):

	chunk_surface = ""
	for morph in chunk1.morphs:
		if morph.pos != "記号":
			# 今までrep1が出てきていない、かつ名詞だったらrep1に変換
			if (morph.pos == "名詞") & (rep1 not in "".join(chunk_pass_list)) & (rep1 not in chunk_surface):
				chunk_surface += rep1
			# 今までrep2が出てきていない、かつ名詞、かつchunk2と一致していたらrep2に変換
			elif (morph.pos == "名詞") & (chunk1 == chunk2) & (rep2 not in chunk_surface):
				chunk_surface += rep2
			else:
	 			chunk_surface += morph.surface
	chunk_pass_list.append(chunk_surface)
	
	# パスをたどって行った先が、chunk2だったらそれを出力して終了
	if chunk1 == chunk2:
		return (1, chunk_pass_list)
	# パスをたどって行った先が、文末だったら
	elif chunk1.dst == -1:
		return (0, chunk_pass_list)
	# 途中だったら次のパスを入力として再帰	
	else:
		return make_pair_pass(sentence_list, sentence_list[chunk1.dst], chunk2, chunk_pass_list, rep1, rep2)

## 1文ずつ見ていく
for sentence_list in all_list:
	chunk_noun_list = []
	for chunk in sentence_list:

		# 今の文節が名詞を含む文節か確認
		pos_list = [morph.pos for morph in chunk.morphs]
		if "名詞" in pos_list:
			chunk_noun_list.append(chunk)

	#print(chunk_noun_list)
	if(chunk_noun_list != []):
		for i in range(len(chunk_noun_list)):
			for j in range(i+1, len(chunk_noun_list)):
				(flag, chunk_pass_list) = make_pair_pass(sentence_list, chunk_noun_list[i], chunk_noun_list[j], [], "X", "Y")
				# 1. もしiとjがつながっていたら
				if flag == 1:
					print(" -> ".join(chunk_pass_list))
				# 2.つながっていなかったら
				else:
					# ダミーのchunk2をおいて、j番目の文節から文末までのパスを取得(この時YとX入れ替え)
					(flag, chunk_pass_list2) = make_pair_pass(sentence_list, chunk_noun_list[j], 0, [], "Y", "X")
					# chunk_pass_list と chunk_pass_list2を比較
					common_list = list(set(chunk_pass_list ) & set(chunk_pass_list2))
					# chunk1から文末までで共通でない部分を出力
					x_pass_list = [chunk for chunk in chunk_pass_list if chunk not in common_list]
					print (" -> ".join(x_pass_list), end = "")
					print (" | ", end = "")
					# chunk2から文末までで共通でない部分を出力
					y_pass_list = [chunk for chunk in chunk_pass_list2 if chunk not in common_list]
					print (" -> ".join(y_pass_list), end = "")
					print (" | ", end = "")
					# 共通部分を出力
					common_pass_list = [chunk for chunk in chunk_pass_list if chunk in common_list]
					print (" -> ".join(common_pass_list), end = "")
					print()