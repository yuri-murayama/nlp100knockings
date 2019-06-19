# -*- coding: utf-8 -*-

INPUT_TEXT_PATH = "./output50.txt"
OUTPUT_TEXT_PATH = "./output51.txt"
fr = open(INPUT_TEXT_PATH, "r")
fw = open(OUTPUT_TEXT_PATH, "w")

lines = fr.readlines()

for line in lines:

    word_list = line.split(" ")
    for w in word_list:
        w = w.replace(",", "").replace(".", "").replace("(", "").replace(")", "")
        fw.write(w+"\n")

fr.close()
fw.close()
