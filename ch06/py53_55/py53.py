import xml.etree.ElementTree as ET

lines = ''
def analyze():
    x = ET.parse('./nlp.txt.xml')
    root = x.getroot()
    line = root.find('document/sentences')
    for i in line.findall('sentence/tokens/token/word'):
        yield i


def main():
    with open('py53.txt', 'w', encoding='utf8') as f:
        for words in analyze():
            w = words.text
            lines = w + '\n'
            f.write(lines)

if __name__ == '__main__':
    main()
