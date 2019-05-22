import re
with open('jawiki-country-EU.json', 'r') as f:
    lines = f.read()
    m1 = re.search(r'(\{\{基礎情報\s国)',lines)
    m2 = re.search(r'\n(\}\})',lines[m1.end():])
    with open('kisojoho.json', 'w') as f2:
        f2.write(lines[m1.end()+1:m2.end()])
        
with open('kisojoho.json','r') as f3:
    lines = f3.read().split('\n')
    dic = {}
    for line in lines:
        m = re.match(r'^(\|)(.*?)\s=\s(.*?)$',line)
        if m != None:
            dic.update([(m.group(2),m.group(3))])
    print(dic)
