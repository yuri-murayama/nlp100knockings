# -*- coding: utf-8 -*-

filepath = "./hightemp.txt"

with open(filepath) as f:
    line = f.read()
    print(line.replace('\t', ' '))
