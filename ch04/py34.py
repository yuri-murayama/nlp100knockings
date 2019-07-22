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

def AofB(lines):
    morpheme = namedtuple('morpheme', ['surface', 'pos'])

    for sentense in lines:
        x = morpheme('', '')
        y = morpheme('', '')

        for word in sentense:
            if word['pos'] == '名詞' and y.surface == 'の' and \
               y.pos == '助詞' and x.pos == '名詞':
                yield x.surface + y.surface + word['surface']
            x = y
            y = morpheme(word['surface'], word['pos'])

def main():
    article = analyze()
    nouns = [surface for surface in AofB(article)]
    print(nouns[:30])

if __name__ == '__main__':
    main()
