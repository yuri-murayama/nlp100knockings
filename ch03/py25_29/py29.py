import json
import gzip
from pprint import pprint
import re
import urllib.request

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
                binfo[result.group(1)] = result.group(2)
                last_index = result.group(1)
        else:

            if re.match("^{{基礎情報 ", line):
                binfo_start = True

    return binfo


def remove_mark(binfo):
    copy = {}
    for key, value in binfo.items():
        value = re.sub("[']{2,4}", "", value)
        copy[key] = value
    return copy

def remove_link(binfo):
    copy = {}
    pattern1 = "\[\[([^:\]|]+)\|([^\]]+)\]\]"
    pattern2 = "\[\[([^:\]|]+)\]\]"

    for key, value in binfo.items():
        value = re.sub(pattern1, "\g<2>", value)
        value = re.sub(pattern2, "\g<1>", value)
        copy[key] = value
    return copy

def remove_markup(binfo):
    copy = {}
    pattern1 = "\[\[ファイル:([^|]+)\|([^|\]]+)\|([^\]]+)\]\]"
    pattern2 = "\{\{lang\|[a-z]{2,}\|([^}]+)\}\}"
    pattern3 = "\[([^ ]+) ([^\]]+)\]"
    pattern4 = "<([a-z]+)( )?/>"
    pattern5 = "<([a-z]+)( [^>]+)?>"
    pattern6 = "</([a-z]+)>"
    for key, value in binfo.items():
        value = re.sub(pattern1, "\g<3>", value)
        value = re.sub(pattern2, "\g<1>", value)
        value = re.sub(pattern3, "\g<2>", value)
        value = re.sub(pattern4, "", value)
        value = re.sub(pattern5, "", value)
        value = re.sub(pattern6, "", value)
        copy[key] = value
    return copy

def image_url(file_name):
    queries = {
        "action": "query",
        "titles": "File:" + urllib.parse.quote(file_name),
        "prop": "imageinfo",
        "iiprop": "url",
        "format": "json",
    }
    url = "https://www.mediawiki.org/w/api.php?" + "&".join([("%s=%s" % (k, v)) for k, v in queries.items()])
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    response = f.read().decode('utf-8')

    return json.loads(response)

if __name__ == '__main__':
    article = country("イギリス")
    binfo = info(article["text"])
    binfo = remove_mark(binfo)
    binfo = remove_link(binfo)
    binfo = remove_markup(binfo)

    result = image_url(binfo["国旗画像"])
    print(result["query"]["pages"]["-1"]["imageinfo"][0]["url"])