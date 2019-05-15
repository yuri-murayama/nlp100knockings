import re

path = "output.txt"

with open(path) as f:
    lines = f.read()


pattern1 = re.compile(r"^\{\{基礎情報.*?$(.*?)^\}\}$", re.MULTILINE | re.DOTALL)

content = pattern1.findall(lines)

pattern2 = re.compile(r"^\|(.+?)\s*=\s*(.+?)((?=\n\|)|(?=\n$))", re.MULTILINE | re.DOTALL)

dict = {}

for c in content:
    m = pattern2.findall(c)

    for mm in m:
        # 強調マークアップ
        mark = re.sub("\'{2,5}", "", mm[1])
        # 内部リンク、ファイル
        link = re.sub("\[\[([^\|]+\|)*?([^\|]+?)\]\]", "\\2", mark)
        # lang
        lang = re.sub("\{\{([^\|]+\|)*?([^\|]+?)\}\}", "\\2", link)
        # URL
        url = re.sub("\[http[^\s]*\s?(.*)\]", "\\1", lang, re.DOTALL)
        # <ref>, <br>
        tag = re.sub("\<.*?\>", "", url)
        dict[mm[0]] = tag
        
# imageinfo
import requests

image = dict["国旗画像"]

S = requests.Session()
URL = "http://www.wikipedia.org/w/api.php?"+"action=query&"+"format=json&"+"prop=imageinfo&"+"titles=File:"+image

R = S.get(url=URL)
DATA = R.json()

id = list(DATA["query"]["pages"].keys())[0]

print("https://en.wikipedia.org/w/index.php?curid="+id)
