import json
import gzip
from pprint import pprint
import re

def country(name):
    f = gzip.open("jawiki-country.json.gz", "rt")
    for line in f:
        article = json.loads(line)
        if article["title"] == name:
            return article
    return {}

def info(text):
    binfo = {}

    binfo_start = False
    last_index = None
    for line in text.split("\n"):
        if binfo_start:

            if re.match("^}}$", line):
                break

            if re.match("^[\*]{1,2}{{", line):
                binfo[last_index] += "\n" + line
                continue


            result = re.match("^\|([^=]+) = (.+)", line)
            if result:
                binfo[result.group(1)] = result.group(2) #groupはmatchした文字列を取得する
                last_index = result.group(1)
        else:

            if re.match("^{{基礎情報 ", line):
                binfo_start = True

    return binfo

if __name__ == '__main__':
    article = country("イギリス")
    pprint(info(article["text"]))
