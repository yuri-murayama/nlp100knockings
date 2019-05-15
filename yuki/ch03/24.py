import re
with open('jawiki-country-EU.json', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        m = re.search(r'(\[\[)?(File|ファイル):(.*?)(\|)', line)
        if m != None:
            print(m.group(3))
