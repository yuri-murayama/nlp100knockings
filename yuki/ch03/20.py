import json

with open('jawiki-country.json', 'r') as f:
    for line in f:
        dic = json.loads(line)
        if dic["title"] == "イギリス":
            with open('jawiki-country-EU.json', 'w') as ff:
                ff.write(dic["text"])
            
#jsonファイルの構成
#{"text":記事,"title":記事名}
