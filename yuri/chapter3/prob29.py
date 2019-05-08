from prob21 import fopen
import re
import requests
import json

def to_text(l):
    l = re.sub(r'\'{2,5}', r'', l) #強調マークアップを除去
    pattern = r'\[\[([^\]]+?\|)*(.*?)\]\]'
    l = re.sub(pattern, r'\2', l) #内部リンクマークアップを除去
    pattern1 = r'{{(.*?\|){2}(.*?)}}'
    l = re.sub(pattern1, r'\2', l) #{{}}を除去
    l = re.sub(r'<.*?>', r'', l) #<br>, <ref>を除去
    l = re.sub(r'\[.*?\]', r'', l) #外部リンクマークアップを除去
    return l

t = fopen()
pattern1 = r'基礎情報.*?^(.*?)^\}\}'
l = re.findall(pattern1, t, flags=re.MULTILINE | re.DOTALL)
pattern2 = r'^\|(.*?)\s\=\s(.*?)$'
l = re.findall(pattern2, l[0], flags=re.MULTILINE)
d = {line[0]: to_text(line[1]) for line in l}

url = "https://en.wikipedia.org/w/api.php"

payload = {
    'format': 'json',
    'action': 'query',
    'prop': 'imageinfo',
    'titles': 'File: {}'.format(d["国旗画像"]),
    'iiprop': 'url'
}

response = requests.get(url, params=payload).text

l = re.findall(r'"url":"(.*?)"', response)

print(l[0])