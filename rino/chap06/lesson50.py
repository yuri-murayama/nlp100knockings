# -*- coding: utf-8 -*-

import re

ENGLISH_TEXT_PATH = "./input/nlp.txt"
english_data = open(ENGLISH_TEXT_PATH, "r")
lines = english_data.readlines()

pattern = re.compile(r'''(^.*?[\.|;|\?|!])\s([A-Z].*)''',
                     re.MULTILINE + re.VERBOSE + re.DOTALL)

text = []

for line in lines:

    line = line.strip()

    while len(line) > 0:
        match = pattern.match(line)

        if match:
            text.append(match.group(1))
            line = match.group(2)

        else:
            text.append(line)
            line = ''

english_data.close()

OUTPUT_TEXT = "output50.txt"
with open(OUTPUT_TEXT, "w") as fw:
    fw.write("\n".join(text))
