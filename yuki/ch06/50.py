#. or ; or : or ? or ! → 空白文字 → 英大文字 を一文として改行
import re

with open('nlp.txt','r') as f:
    with open('output50.txt','w') as outputf:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == '':
                continue
            else:
                line = re.sub(r'([\.|;|:|!])\s([A-Z])',r'\1\n\2',line) #[A-Z] = \u
            outputf.write(line+'\n')
