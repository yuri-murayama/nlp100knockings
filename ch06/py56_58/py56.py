import re
import xml.etree.ElementTree as ET

class Coreference:
    def __init__(self, filepath):
        x = ET.parse(filepath)
        root = x.getroot()
        self.sentences = root.find('document/sentences')
        self.coreference = root.find('document/coreference')

    def num(self):
        for i in self.coreference:
            yield i


# mentionのtext -> representativeMention置き換える
    def replace_mention(self, mention, representativeMention):
        sentence_id = mention.find('sentence').text
        start_id = mention.find('start').text
        end_id = str(int(mention.find('end').text) - 1)
        target = self.sentences.find("sentence[@id='" + sentence_id  + "']")
        start = target.find("tokens/token[@id='" + start_id + "']")
        end = target.find("tokens/token[@id='" + end_id + "']")

        text = representativeMention.find('text').text

        start_word = start.find('word')
        start_word.text = '「{}({}'.format(text, start_word.text)

        end_word = end.find('word')
        end_word.text = end_word.text + ')」'


    def replace(self):
            for cf in self.num():
                rm = cf.find("mention[@representative='true']")
                for m in cf.findall('mention'):
                    if 'representative' in m.attrib:
                        continue
                        self.replace_mention(m, rm)

    def write_text(self):
        with open('py56.txt', 'w', encoding='utf8') as w:
            prev = ''
            for e in self.sentences.findall('sentence/tokens/token'):
                word = e.find('word').text
                if word == '-LRB-':
                    word = '('
                elif word == '-RRB-':
                    word = ')'
                if word == '.':
                    w.write(word + '\n')
                elif word == ',' or word == '?' or word == '\'' or word == ')':
                    w.write(word)
                elif word == '(':
                    prev = word
                else:
                    if prev == '(':
                        w.write(' (' + word)
                    else:
                        w.write(' ' + word)
                    prev = ''

def main():
    line = Coreference('nlp.txt.xml')
    line.replace()
    line.write_text()

if __name__ == '__main__':
    main()
