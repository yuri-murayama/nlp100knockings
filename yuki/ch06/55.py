#入力文中の人名をすべて抜き出せ
from xml.etree import ElementTree
tree_parse = ElementTree.parse('nlp.txt.xml')
with open('output55.txt','w') as f:
    word_list= []
    ner_list = []
    for word in tree_parse.iter('word'):
        word_list.append(word.text)
    for ner in tree_parse.iter('NER'):
        ner_list.append(ner.text)
    for i, ner in enumerate(ner_list):
        if ner == 'PERSON':
            f.write(word_list[i]+'\n')
