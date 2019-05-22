from prob30 import load_neko

text = load_neko()
lst = []
for sentence in text:
    for morpheme in sentence:
        if morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続':
            lst.append(morpheme['surface'])

print(lst)