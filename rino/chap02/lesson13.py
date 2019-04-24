# -*- coding: utf-8 -*-

# UNIX
# paste col1.txt col2.txt > hightemp_13.txt

COL1_FILE = "./col1.txt"
COL2_FILE = "./col2.txt"
OUTPUT_FILE = "hightemp_13.txt"

l = []
with open(COL1_FILE) as f1:
   col1 = f1.read().split("\n")

with open(COL2_FILE) as f2:
   col2 = f2.read().split("\n")

with open(OUTPUT_FILE, "w") as fw:
    for c1, c2 in zip(col1, col2):
        fw.write("{}\t{}\n".format(c1, c2))
