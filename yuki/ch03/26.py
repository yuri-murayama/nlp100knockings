import re

dic = {}
with open('kisojoho.json', 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        m = re.match(r'^\|(.*?)\s=\s(.*?)$',line)
        if m != None:
            dic.update([(m.group(1),re.sub(r"\'{2,5}",r"",m.group(2)))])
    print(dic)


