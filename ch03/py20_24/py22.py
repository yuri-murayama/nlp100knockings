import gzip
import json
import re

def country(name):
    f = gzip.open("jawiki-country.json.gz", "rt")
    for line in f:
        article = json.loads(line)
        if article["title"] == name:
            return article
    return {}

def category_name(text):
    categories = []
    for line in text.split("\n"):
        new_cate = re.match("\[\[Category:([^|]+)(|.*)?\]\]", line)
        if new_cate:
            categories.append(new_cate.group(1))
    return categories

if __name__ == '__main__':
    article = country("イギリス")
    for line in category_name(article["text"]):
        print(line)
