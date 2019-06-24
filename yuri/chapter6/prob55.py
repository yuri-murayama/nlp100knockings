import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

with open('output55.txt', 'w') as f:
    for token in tree.iter('token'):
        ner = token.find('NER').text
        if ner == 'PERSON':
            name = token.find('word').text
            f.write(name + '\n')