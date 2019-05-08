#-*- coding: utf-8 -*-

import json

path = "./jawiki-country.json"
lst = []
with  open(path) as f:
    for line in f:
        json_dict = json.loads(line)
        if json_dict["title"] =="イギリス":
            lst.append(json_dict["text"])

with open("output.txt", mode='w') as f:
    f.writelines(lst)
