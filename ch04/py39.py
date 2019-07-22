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

def frequency(lines):
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

def getScatterData(words):
    data = [x[1] for x in words.items()]
    data = sorted(data, key=lambda x: x, reverse=True)
    return range(1, len(data)+1), data

def plotScatter(x, y):
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.scatter(x, y, s=2)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel('頻度順位')
    plt.ylabel('頻度')
    plt.show()

def main():
    article = analyze()
    words = frequency(article)
    x, y = getScatterData(words)
    plotScatter(x, y)

if __name__ == '__main__':
    main()
