from xml.etree import ElementTree
tree_parse = ElementTree.parse('nlp.txt.xml')
with open('output53.txt','w') as f:
    for word in tree_parse.iter('word'):
        f.write(word.text+'\n')
