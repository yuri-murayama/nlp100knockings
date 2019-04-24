# -*- coding: utf-8 -*-

filepath = "./hightemp.txt"

with open(filepath) as f:
    lines = f.readlines()

print(len(lines))
