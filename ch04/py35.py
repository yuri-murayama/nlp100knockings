import re
from collections import namedtuple

def analyze():
    lines = []
    sentence = []
    with open('neko.txt.mecab',encoding='utf-8') as f:
        for line in f:
            words = re.split(r'\t|,|\n',line)
            if words[0] == 'EOS':
                if sentence:
                    lines.append(sentence)
                    sentence = []
                continue
            sentence.append({
                "surface": words[0],
                "base": words[7],
                "pos": words[1],
                "pos1": words[2],
            })
    return lines

def long_noun(lines):
    for sentense in lines:
        noun = ''
        count = 0
        for word in sentense:
            if word['pos'] == '名詞' and (noun != '' or word['pos1'] != '副詞可能'):
                noun += word['surface']
                count += 1
            else:
                if count > 1:
                    yield noun
                noun = ''
                count = 0

def main():
    article = analyze()
    nouns = [surface for surface in long_noun(article)]
    print(nouns[:30])

if __name__ == '__main__':
    main()
