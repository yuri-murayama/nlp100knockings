#-*- coding: utf-8 -*-
#58. タプルの抽出

from xml.etree import ElementTree

# XMLファイルを解析
tree = ElementTree.parse('nlp.txt.new.xml')

# XMLを取得
root = tree.getroot()

for dependencies in root.iter("dependencies"):

	nsubj_dict = {} #nsubj関係の子を持つ単語とその子を保存
	dobj_dict = {} #dobj関係の子を持つ単語とその子を保存

	if dependencies.attrib.get("type") == "collapsed-dependencies":

		for dep in dependencies.iter("dep"):
			if dep.attrib.get("type")  == "nsubj":
				nsubj_dict[dep.find("governor").text] = dep.find("dependent").text
			if dep.attrib.get("type")  == "dobj":
				dobj_dict[dep.find("governor").text] = dep.find("dependent").text
				
		# nsubj関係の子とdobjの関係の子の両方を持つ述語だけ取り出す(出現順番は保つ)
		predicates = sorted(set(nsubj_dict.keys()) & set(dobj_dict.keys()), key=list(nsubj_dict.keys()).index)

		for pred in predicates: #各述語について主語と目的語とともに出力
			print(nsubj_dict[pred] + '\t' + pred + '\t' + dobj_dict[pred])