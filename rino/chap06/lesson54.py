# -*- coding: utf-8 -*-

from xml.etree import ElementTree

INPUT_XML_PATH = "./nlp.txt.xml"
OUTPUT_TEXT_PATH = "./output54.txt"
fw = open(OUTPUT_TEXT_PATH, "w")

# XML ファイルから ElementTree オブジェクトを生成
tree = ElementTree.parse(INPUT_XML_PATH)

# 先頭要素を表す Element オブジェクトを取得
elem = tree.getroot()

for token in elem.iter('token'):
    fw.write("{}\t{}\t{}\n".format(token.find('word').text,
                                   token.find('lemma').text,
                                   token.find('POS').text))

fw.close()
