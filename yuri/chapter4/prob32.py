from prob30 import load_neko

text = load_neko()
lst = []
for sentence in text:
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            lst.append(morpheme['base'])

print(lst)