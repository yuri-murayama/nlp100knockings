#-*- coding: utf-8 -*-
#30. 形態素解析結果の読み込み

def make_list():

	all_list = [] #全ての文についての形態素情報を入れたリスト
	sentence_list = [] #1文の形態素情報を入れたリスト

	# ファイルの読み込み
	with open("neko.txt.mecab", mode = 'r') as f:
		for line in f:
			# 改行を除く
			line = line.strip()
			# 文末まで行う
			if line != 'EOS':
				#print(line)
				# 表層系とそれ以外に分ける
				line = line.split('\t')
				# 空白の場合は、表層系に空白を入れる
				if len(line) == 1:
					line.insert(0, ' ')
				surface = line[0]
				other = line[1].split(',')

				map_dict = {}
				map_dict['surface'] = surface
				map_dict['base'] = other[6]
				map_dict['pos'] = other[0]
				map_dict['pos1'] = other[1]

				sentence_list.append(map_dict)

			# 文末だったら
			else:
				# all_listに加える
				all_list.append(sentence_list)
				# sentence_listをリセット
				sentence_list = []

	#最後でEOSが2回続くので、最後を削除
	all_list.pop()

	return all_list

if __name__ == '__main__':
	all_list = make_list()
	print(all_list)


		