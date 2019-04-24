# -*- coding: utf-8 -*-

# UNIX
# sort col1.txt | uniq

INPUT_FILE = "hightemp.txt"

with open(INPUT_FILE) as f:
   col1_list = []
   for line in f:
      col1 = line.split("\t")[0]
      if col1 not in col1_list:
         col1_list.append(col1)

print(col1_list)
