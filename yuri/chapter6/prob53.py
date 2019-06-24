import xml.etree.ElementTree as ET

# ./corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt 
tree = ET.parse('nlp.txt.xml')

with open('output53.txt', 'w') as f:
    for word in tree.iter('word'):
        f.write(word.text + '\n')