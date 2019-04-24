# -*- coding: utf-8 -*-

# UNIX
# sort col1.txt | uniq -c | sort -n -r

INPUT_FILE = "hightemp.txt"

col1_dict = {}
with open(INPUT_FILE) as f:
   for line in f:
      col1 = line.split("\t")[0]

      if col1 not in col1_dict:
         col1_dict[col1] = 1
      else:
         col1_dict[col1] += 1

for col1, num in sorted(col1_dict.items(), key=lambda x: -x[1]):
   print(col1)
