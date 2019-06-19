# -*- coding: utf-8 -*-

from stemming.porter2 import stem

INPUT_TEXT_PATH = "./output51.txt"
OUTPUT_TEXT_PATH = "./output52.txt"
fr = open(INPUT_TEXT_PATH, "r")
fw = open(OUTPUT_TEXT_PATH, "w")

words = fr.readlines()

for w in words:
    w = w.rstrip('\n')
    s = stem(w)
    fw.write("{}\t{}\n".format(w, s))

fr.close()
fw.close()
