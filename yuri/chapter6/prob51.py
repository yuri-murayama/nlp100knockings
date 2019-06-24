import re

with open('output50.txt') as f:
    lines = f.readlines()

with open('output51.txt', 'w') as f:
    for line in lines:
        line = re.sub(r'(.*?)\s(.*?)', r'\1\n\2', line)
        f.write(line + '\n')