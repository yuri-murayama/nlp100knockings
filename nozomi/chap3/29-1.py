import re
import requests
import json

with open('uk_kiso.txt','r') as f,open('field.txt','w') as f1,open('atai.txt','w') as f2:
    ls = f.readlines()
    for l in ls:
        m0 =re.sub(r'(\'\'\')|(\'\'\')','',l)
        m1 =re.sub(r'(\[\[)(.+)\|','',m0)
        m2 =re.sub(r'(\[\[)|(\]\])','',m1)
        m3 =re.sub(r'(<ref)(.+)(IMF)','',m2)
        m4 =re.sub(r'(<ref)(.+)(htm)','',m3)
        m = re.match(r'^\|(.+?)(=+)(.+)$',m4)
        if m != None:
            f1.write(m.group(1).strip()+'\n')
            f2.write(m.group(3).strip()+'\n')

with open('field.txt','r') as f1,open('atai.txt','r') as f2:
    l1 = f1.read().split('\n')
    l2 = f2.read().split('\n')
    d = dict(zip(l1,l2))
    d.pop('')
    #print(d['国旗画像'])
    img = d['国旗画像']

url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(img),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

r = requests.get(url, params=payload)
text = r.text
#print(text)
#print(text[168:245])
#print(text['url'])
#print(r,url)
#print(r['url'],url)
m = re.findall(r'"url":"(.+?)",',text)
#print(m)
if m != None:
    print(m)
