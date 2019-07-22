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

def histo_data(words):
    hist = {}
    for word in words.items():
        if word[1] in hist.keys():
            hist[word[1]] += 1
        else:
            hist[word[1]] = 1
    return words

def histo(data):
    xs = [x[1] for x in data]

    plt.rcParams['font.family'] =  'AppleGothic'

    plt.hist(xs, bins=25, range=(1, 25))
    plt.xlim(xmin=1, xmax=25)
    plt.xlabel('出現頻度')
    plt.ylabel('種類')
    plt.show()



def main():
    article = analyze()
    words = frequency(article)
    histdata = histo_data(words)
    sorteddata = sorted(histdata.items(), key=lambda x: x[1], reverse=True)
    print(sorteddata[0:20])

    histo(sorteddata)

if __name__ == '__main__':
    main()
