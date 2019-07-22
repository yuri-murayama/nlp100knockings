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

def section(text):
    sections = []
    for line in text.split("\n"):
        if re.match("^[=]{2,}([^=]+)[=]{2,}$", line):
            sections.append(line)
    return sections

def level(line):
    if re.match("^==[^=]", line):
        return 1
    if re.match("^===[^=]", line):
        return 2
    if re.match("^====[^=]", line):
        return 3
    if re.match("^=====[^=]", line):
        return 4

def section_name(line):
    result = re.match("^[=]{2,}([^=]+)[=]{2,}$", line)
    return result.group(1)


if __name__ == '__main__':
    article = country("イギリス")
    for line in section(article["text"]):
        print(section_name(line) + ":" + str(level(line)))
