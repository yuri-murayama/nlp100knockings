#-*- coding: utf-8 -*-
#係り受け解析結果の読み込み（文節・係り受け)

from prob40 import Morph

class Chunk:

	def __init__(self, morphs, dst, srcs):
        
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs

def make_chunk_list():

	all_list = [] #全ての文についての形態素情報を入れたリスト
	sentence_list = [] #1文の文節情報を入れたリスト
	morph_list = [] #文節の単語情報を入れたリスト
	morph_list_sentence = [] #1文の単語情報を入れたリスト
	kakarisaki_dict = {} #1文の中の係先の情報を入れたリスト key:係元文節番号 value:係先文節番号
	kakarimoto_dict = {} #1文の中の係元の情報を入れたリスト key:係先文節番号 value:係元文節番号のリスト

	# ファイルの読み込み
	with open("neko.txt.cabocha", mode = 'r') as f:
		for line in f:
			# 改行を除く
			line = line.strip()
			# 文末まで行う
			if line != 'EOS':
				# 1.文節の中身を表している行だったら
				if line[0] != '*':
					# 表層系とそれ以外に分ける
					line = line.split('\t')
					# 空白の場合は、表層系に空白を入れる
					if len(line) == 2:
						line.insert(0, ' ')
					surface = line[0]
					other = line[1].split(',')

					morph_list.append(Morph(surface, other[6], other[0], other[1]))
				# 2.文節の情報を表している行だったら
				else:
					# morph_listに今まで見ていた文節の単語情報を加える
					if morph_list != []:
						morph_list_sentence.append(morph_list)
					# 文節情報をリストに分割	
					line = line.split(' ')

					num_own = int(line[1]) #今の文節番号
					num_kakarisaki = int(line[2][:-1]) #係先の文節番号
					kakarisaki_dict[num_own] = num_kakarisaki #係先の文節番号保存
					

					# もし係先が文末でなかったら今の文節番号を係先の係元とする
					if num_kakarisaki != -1:
						if num_kakarisaki in kakarimoto_dict.keys():
							kakarimoto_dict[num_kakarisaki].append(num_own)
						else:
							kakarimoto_dict[num_kakarisaki] = [num_own]

					# morph_listをリセット
					morph_list = []			

			# 文末だったら
			else:
				# 今まで見ていた文節の単語情報追加
				if morph_list != []:
						morph_list_sentence.append(morph_list)
				# もし1つ前も文末でなかったらsentence_list作成
				if morph_list_sentence != []:
					# 1文ずつsentence_list作成	
					for i in kakarisaki_dict.keys():
						# i番目の文節の係元があった場合
						if i in kakarimoto_dict.keys():
							chunk = Chunk(morph_list_sentence[i], kakarisaki_dict[i], kakarimoto_dict[i])
						else: #i番目の文節の係元がなかった場合
							chunk = Chunk(morph_list_sentence[i], kakarisaki_dict[i], [])
						sentence_list.append(chunk)
					# all_listに加える
					all_list.append(sentence_list)		

				# 全てのリスト、辞書をリセット	
				# morph_list_sentenceをリセット
				morph_list_sentence = []
				morph_list = []
				# sentence_listをリセット
				sentence_list = []
				# kakarisaki_dictをリセット
				kakarisaki_dict = {}
				# kakarimoto_dictをリセット
				kakarimoto_dict = {}

	#最後でEOSが2回続くので、最後を削除
	all_list.pop()

	return all_list

if __name__ == '__main__':
	# Morphオブジェクトのリストを作成
	all_list = make_chunk_list()
	# 8文目を表示
	print("-----------------------------")
	for i, chunk in enumerate(all_list[7]):
		print ("文節{}".format(i))
		for morph in chunk.morphs:
			print(morph.surface, morph.base, morph.pos, morph.pos1)
		print("係先 : {}".format(chunk.dst))
		print("係元 : {}".format(chunk.srcs))
		print("-----------------------------")
