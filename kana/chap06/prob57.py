#-*- coding: utf-8 -*-
#57. 係り受け解析

from xml.etree import ElementTree
import pydot

# XMLファイルを解析
tree = ElementTree.parse('nlp.txt.new.xml')

# XMLを取得
root = tree.getroot()


# 係り受けの関係を文ごとにリストに
dependencies_all = []
for dependencies in root.iter("dependencies"):
	dependencies_sentence = []
	if dependencies.attrib.get("type") == "collapsed-dependencies":
		for dep in dependencies.iter("dep"):
			dependencies_sentence.append((" " + dep.find("governor").text, " " + dep.find("dependent").text))
		dependencies_all.append(dependencies_sentence)

# 全ての文についてそれぞれ1つずつのファイルに出力
for i, dependencies_sentence in enumerate(dependencies_all):
	# pydot グラフの準備
	G = pydot.Dot(graph_type='digraph')
	G.set_node_defaults(shape='circle')
	# 文ごとにプロット
	for dependent in dependencies_sentence:
		G.add_edge(pydot.Edge(dependent[0], dependent[1]))
	G.write_png('./output57/dependency_tree_' + str(i + 1) + '.png')			