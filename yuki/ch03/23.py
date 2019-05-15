import re
with open('jawiki-country-EU.json', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        m = re.match(r'^(={2,})\s*(.+?)\s*(={2,})$', line)
        if m != None:
            level = m.group(1).count('=')
            print(m.group(2)+str(level))
        
