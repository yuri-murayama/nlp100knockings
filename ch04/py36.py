import re
from collections import namedtuple
import matplotlib.pyplot as plt

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

def freqency(lines):
    words = {}
    for sentense in lines:
        for word in sentense:
            if word['pos'] == '記号':
                continue
            if word['surface'] in words.keys():
                words[word['surface']] += 1
            else:
                words[word['surface']] = 1
    return words

def main():
    article = analyze()
    words = freqency(article)
    swords = sorted(words.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 20):
        print(i, swords[i][0], swords[i][1])

if __name__ == '__main__':
    main()
