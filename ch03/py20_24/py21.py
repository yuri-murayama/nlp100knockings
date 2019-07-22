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

def category(text):
    categories = []
    for line in text.split("\n"):
        if re.match("\[\[Category:(.+)?\]\]", line):
            categories.append(line)
    return categories

if __name__ == '__main__':
    article = country("イギリス")
    for line in category(article["text"]):
        print(line)
