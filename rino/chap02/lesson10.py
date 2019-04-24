# -*- coding: utf-8 -*-

# UNIX
# wc -l hightemp.txt  # 24

TEXT_FILE = "./hightemp.txt"

with open(TEXT_FILE) as f:
    l = f.readlines()
    print(len(l))
