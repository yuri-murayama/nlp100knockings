# -*- coding: utf-8 -*-

# UNIX
# expand -t 1 hightemp.txt > hightemp_11.txt

TEXT_FILE = "./hightemp.txt"
OUTPUT_FILE = "./hightemp_11.txt"

l = []
with open(TEXT_FILE) as f:
    for line in f:
        replaced_line = line.replace('\t', ' ')
        l.append(replaced_line)

with open(OUTPUT_FILE, 'w') as fw:
    fw.write(''.join(l))
