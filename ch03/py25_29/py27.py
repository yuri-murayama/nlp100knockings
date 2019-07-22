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

if __name__ == '__main__':
    article = country("イギリス")
    binfo = info(article["text"])
    binfo = remove_mark(binfo)
    binfo = remove_link(binfo)
    pprint(binfo)
