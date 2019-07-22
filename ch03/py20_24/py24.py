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


def media(text):
    medias = []
    for line in text.split("\n"):
        m_file = re.match(".*(\[\[)?ファイル:([^|]+)", line)
        if m_file:
            medias.append(m_file.group(2))
        else:
            m_file = re.match(".* = ([^.]+\.svg)", line)
            if m_file:
                medias.append(m_file.group(1))
    return medias

if __name__ == '__main__':
    article = country("イギリス")
    for line in media(article["text"]):
        print(line)
