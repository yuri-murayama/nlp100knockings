import re

with open('nlp.txt') as f:
    lines = f.readlines()

with open('output50.txt', 'w') as f:
    for line in lines:
        line = line.strip('\n')
        line = re.sub(r'([.;:?!])\s([A-Z])', r'\1\n\2', line)   
        f.write(line + '\n')