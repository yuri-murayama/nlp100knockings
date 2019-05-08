import re
with open('jawiki-country-EU.json', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        if "Category" in line:
            m = re.match(r'^\[\[Category:(.*)\]\]$', line)
            print(m.group(1).split('|')[0])

