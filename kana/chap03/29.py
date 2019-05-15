#-*- coding: utf-8 -*-
#29. 国旗画像のURLを取得する

import re
import requests

#ファイルの読み込み
with open("article.txt", mode = 'r') as f:
	text = ''.join(f)

#国旗画像のファイル名取得
[file] = re.findall(r'^\|国旗画像\s\=\s(.*?)$', text, flags = re.MULTILINE)

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "titles":"File:" + file,
    "iiprop" : "url"
}

R = S.get(url=URL, params=PARAMS)
text = R.text
[url] = re.findall(r'\"url\":\"(.*?)\"',text)

print(url)



