# -*- coding: utf-8 -*-

from xml.etree import ElementTree

INPUT_XML_PATH = "./nlp2.txt.xml"
OUTPUT_TEXT_PATH = "./output58.txt"
fw = open(OUTPUT_TEXT_PATH, "w")

# XML ファイルから ElementTree オブジェクトを生成
tree = ElementTree.parse(INPUT_XML_PATH)

# 先頭要素を表す Element オブジェクトを取得
elem = tree.getroot()

for sentence in elem.iter('sentence'):

    if sentence.attrib == {}:
        continue

    # depの辞書のリストを作成
    # {'take': {'nsubj': 'algorithms', 'dobj': 'set'}}
    dep_dict = {}
    for dependencies in sentence.iter('dependencies'):
        if dependencies.attrib['type'] == 'collapsed-dependencies':
            for dep in dependencies.iter('dep'):

                if dep.attrib['type'] == 'nsubj':
                    gov_text = dep.find('governor').text

                    if gov_text not in dep_dict:
                        dep_dict[gov_text] = {}

                    dep_dict[gov_text]['nsubj'] = dep.find('dependent').text

                if dep.attrib['type'] == 'dobj':
                    gov_text = dep.find('governor').text

                    if gov_text not in dep_dict:
                        dep_dict[gov_text] = {}

                    dep_dict[gov_text]['dobj'] = dep.find('dependent').text

    # タブ区切り形式で出力
    for k, d in dep_dict.items():
        if d.get('nsubj') != None and d.get('dobj') != None:
            fw.write("{}\t{}\t{}\n".format(d['nsubj'], k, d['dobj']))
