import re
from nltk.stem.porter import PorterStemmer as PS

# stemming -> 英単語から語幹(stem)を取りだすこと
ps = PS()
lins = ''
with open('py51.txt', 'r', encoding='utf8') as f:
    with open('py52.txt', 'w', encoding='utf8') as f2:
        for line in f:
            words = re.split(r'\n', line)
            #print(words)
            text = ''.join(words)
            sm = ps.stem(text)
            lines = text + '\t' +sm + '\n'
            #print(lines)
            f2.write(lines)
