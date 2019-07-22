import gzip
import json

f = 'jawiki-country.json.gz'

fi =  gzip.open(f, 'rt')
for line in fi:
    d_js = json.loads(line)
    if d_js['title'] == 'イギリス':
        print(d_js['text'])
        break
