# -*- coding: utf-8 -*-

# UNIX
# cut -f 1 -d " " hightemp_11.txt > col1.txt
# cut -f 2 -d " " hightemp_11.txt > col2.txt

INPUT_FILE = "./hightemp_11.txt"
COL1_FILE = "./col1.txt"
COL2_FILE = "./col2.txt"

col1 = []
col2 = []
with open(INPUT_FILE) as f:
    for line in f:
        col_list = line.split(" ")
        col1.append(col_list[0])
        col2.append(col_list[1])

with open(COL1_FILE, 'w') as fw:
    fw.write('\n'.join(col1))

with open(COL2_FILE, 'w') as fw:
    fw.write('\n'.join(col2))
