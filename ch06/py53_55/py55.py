import re
import xml.etree.ElementTree as ET


#lines = ''
def analyze():
    x = ET.parse('nlp.txt.xml')
    root = x.getroot()
    line = root.find('document/sentences')
    for i in line.findall('sentence/tokens/token'):
        if i.find('NER').text == 'PERSON':
            yield i.find('word')


def main():
    with open('py55.txt','w',encoding='utf8') as f:
        for word in analyze():
            name = word.text
            #print(name)
            f.write(name + '\n')

if __name__ == '__main__':
    main()
