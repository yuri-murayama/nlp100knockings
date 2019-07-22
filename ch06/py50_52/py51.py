import re

text = ''
with open('py50.txt', 'r', encoding='utf8') as f:
    with open('py51.txt', 'w', encoding='utf8') as f2:
        for line in f:
            words = re.split(r'\.|\s|,|"|"|\?',line)
            text = '\n'.join(words)
            #print(text)
            f2.write(text)
