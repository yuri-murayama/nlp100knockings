#単語，レンマ，品詞をタブ区切り形式で出力せよ．
from xml.etree import ElementTree
tree_parse = ElementTree.parse('nlp.txt.xml')
word_list=[]
lemma_list = []
pos_list = []
with open('output54.txt','w') as f:
    for word in tree_parse.iter('word'):
        word_list.append(word.text)
    for lemma in tree_parse.iter('lemma'):
        lemma_list.append(lemma.text)
    for pos in tree_parse.iter('POS'):
        pos_list.append(pos.text)
    for i in range(len(word_list)):
        f.write(word_list[i]+'\t'+lemma_list[i]+'\t'+pos_list[i]+'\n')
