from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
with open('output51.txt','r') as f:
    lines = f.readlines()
    with open('output52.txt','w') as outputf:
        for line in lines:
            line = line.strip()
            outputf.write(line+'\t'+porter.stem(line)+'\n')
