import re

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

def verbs_sa(lines):
    for sentense in lines:
        wc = filter(lambda x: x['pos'] == '名詞' and x['pos1'] == 'サ変接続', sentense)
        yield from map(lambda x: x['surface'], wc)

def main():
    article = analyze()
    verbs = [surface for surface in verbs_sa(article)]
    print(verbs[:30])

if __name__ == '__main__':
    main()
