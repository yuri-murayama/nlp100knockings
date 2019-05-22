from prob30 import load_neko

text = load_neko()
lst = []
for sentence in text:
    for i in range(len(sentence)-2):
        if sentence[i]['pos'] == '名詞' and sentence[i+1]['surface'] == 'の' and sentence[i+2]['pos'] == '名詞':
            lst.append(sentence[i]['surface'] + sentence[i+1]['surface'] + sentence[i+2]['surface'])

print(lst)