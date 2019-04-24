# -*- coding: utf-8 -*-

# UNIX
# sort -k 3 -t " " hightemp_11.txt -r > hightemp_18.txt

INPUT_FILE = "hightemp.txt"
OUTPUT_FILE = "hightemp_18.txt"

col_list = []
with open(INPUT_FILE) as f:
   for line in f:
      a,b,c,d = line.split("\t")
      col_list.append((a,b,c,d))

sorted_col_list = sorted(col_list, key=lambda col: col[2], reverse=True)
sorted_col_list_string = ["{}\t{}\t{}\t{}".format(a,b,c,d) \
                          for a,b,c,d in sorted_col_list]

with open(OUTPUT_FILE, "w") as fw:
   fw.write("".join(sorted_col_list_string))
