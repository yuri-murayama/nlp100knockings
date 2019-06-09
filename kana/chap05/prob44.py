#-*- coding: utf-8 -*-
#44. 係り受け木の可視化

#from prob41 import make_chunk_list
from graphviz import Digraph
from prob41 import Chunk
import CaboCha

def make_chunk(tree):
	# 形態素を結合しつつ[{c:文節, to:係り先id}]の形に変換する
	chunks = []
	text = ""
	toChunkId = -1
	for i in range(0, tree.size()):
		token = tree.token(i)
		text = token.surface if token.chunk else (text + token.surface) 
		toChunkId = token.chunk.link if token.chunk else toChunkId
		# 文末かchunk内の最後の要素のタイミングで出力
		if i == tree.size() - 1 or tree.token(i+1).chunk:
			chunks.append({'c': text, 'to': toChunkId})

	return chunks

## 対象文の入力
sentence = input()

## 係り受け情報を取得
c = CaboCha.Parser()

# プログラム的に処理しやすいフォーマットにして、Chunk_list作成
tree =  c.parse(sentence)
chunks = make_chunk(tree)

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')


# ノードの追加
for chunk in chunks:
	G.node(chunk['c'], chunk['c'])

# 係り元→係り先の形式で辺を追加
for chunk in chunks:
	if chunk['to'] >= 0:
		G.edge(chunk['c'],chunks[chunk['to']]['c'])


# print()するとdot形式で出力される
print(G)

# tree.pngで保存
G.render('tree')