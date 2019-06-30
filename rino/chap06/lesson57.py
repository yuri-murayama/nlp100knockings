# -*- coding: utf-8 -*-

from graphviz import Digraph
from xml.etree import ElementTree

INPUT_XML_PATH = "./nlp2.txt.xml"

# XML ファイルから ElementTree オブジェクトを生成
tree = ElementTree.parse(INPUT_XML_PATH)

# 先頭要素を表す Element オブジェクトを取得
elem = tree.getroot()

for sentence in elem.iter('sentence'):

    if sentence.attrib == {}:
        continue

    # formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
    G = Digraph(format='png')
    G.attr('node', shape='circle')

    # エッジの追加
    for dependencies in sentence.iter('dependencies'):
        if dependencies.attrib['type'] == 'collapsed-dependencies':
            for dep in dependencies.iter('dep'):
                gov_text = dep.find('governor').text
                dep_text  = dep.find('dependent').text
                G.edge(gov_text, dep_text)

    # ./lesson57output/(sentence_id).pngで保存する
    sentence_id = sentence.attrib['id']
    output_tree_path = "./lesson57output/{}".format(sentence_id)
    G.render(output_tree_path)
