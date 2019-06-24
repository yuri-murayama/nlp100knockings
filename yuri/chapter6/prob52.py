from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

with open('output51.txt') as f:
    lines = f.readlines()

with open('output52.txt', 'w') as f:
    for line in lines:
        line = line.strip('\n')
        f.write(line + '\t' + ps.stem(line) + '\n')