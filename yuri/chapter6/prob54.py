import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

with open('output54.txt', 'w') as f:
    for token in tree.iter('token'):
        word = token.find('word').text
        lemma = token.find('lemma').text
        pos = token.find('POS').text
        f.write(word+'\t'+lemma+'\t'+pos+'\n')