import re
dic = {}

def remove(s):
    s = re.sub(r'\'{2,5}',r"",s)
    s = re.sub(r"\[\[([^|\]]+?\|)*(.+?)\]\]",r"\2",s)
    return s
with open('kisojoho.json' ,'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        m = re.match(r'^\|(.*?)\s=\s(.*?)$',line)
        if m != None:
            dic.update([(m.group(1),remove(m.group(2)))])            
    print(dic)
