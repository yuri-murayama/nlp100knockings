#-*- coding: utf-8 -*-
#40.係り受け解析結果の読み込み（形態素）


class Morph:

	def __init__(self, surface, base, pos, pos1):
        
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1


def make_list():

	all_list = [] #全ての文についての形態素情報を入れたリスト
	sentence_list = [] #1文の形態素情報を入れたリスト

	# ファイルの読み込み
	with open("neko.txt.cabocha", mode = 'r') as f:
		for line in f:
			# 改行を除く
			line = line.strip()
			# 文末まで行う
			if line != 'EOS' and line[0] != '*':
				# 表層系とそれ以外に分ける
				line = line.split('\t')
				# 空白の場合は、表層系に空白を入れる
				if len(line) == 2:
					line.insert(0, ' ')
				surface = line[0]
				other = line[1].split(',')

				sentence_list.append(Morph(surface, other[6], other[0], other[1]))

			# 文末だったら
			else:
				# もし1つ前も文末でなかったらall_listに加える
				if sentence_list != []:
					all_list.append(sentence_list)
				# sentence_listをリセット
				sentence_list = []

	#最後でEOSが2回続くので、最後を削除
	all_list.pop()

	return all_list

if __name__ == '__main__':
	# Morphオブジェクトのリストを作成
	all_list = make_list()
	# 3文目を表示
	for word in all_list[2]:
		print(word.surface, word.base, word.pos, word.pos1)


"""
==========
出力結果	
==========
吾輩 吾輩 名詞 代名詞
は は 助詞 係助詞
"""	