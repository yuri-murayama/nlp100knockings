from prob30 import load_neko

text = load_neko()
noun_lst = []
connection_lst = []

for sentence in text:
    for morpheme in sentence:
        if morpheme['pos'] == '名詞':
            noun_lst.append(morpheme['surface'])
        else:
            if len(noun_lst) > 1:
                connection_lst.append(''.join(noun_lst))
                noun_lst = []

print(connection_lst)