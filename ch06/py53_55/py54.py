import re
import xml.etree.ElementTree as ET


lines = ''
def analyze():
    x = ET.parse('nlp.txt.xml')
    root = x.getroot()
    line = root.find('document/sentences')
    for i in line.findall('sentence/tokens/token'):
        yield i.find('word'), i.find('lemma'), i.find('POS')

def main():
    with open('py54.txt', 'w', encoding='utf8') as f:
        for word, lemma, pos in analyze():
            w = word.text
            l = lemma.text
            p = pos.text
            n = re.search(r'[A-Z]', p)
            if n:
                lines = w + '\t' + l + '\t' + p + '\n'
                f.write(lines)


if __name__ == '__main__':
    main()
