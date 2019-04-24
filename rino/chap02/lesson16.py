# -*- coding: utf-8 -*-

# UNIX
# split -n <num> hightemp.txt > hightemp_16.txt

# 実行コマンド
# python lesson16.py <num>

import sys

args = sys.argv  # コマンドライン引数
num = int(args[1])

INPUT_FILE = "hightemp.txt"

with open(INPUT_FILE) as f:
   line_list = f.read().split("\n")

length = len(line_list)

# 割り切れるかどうか？
if length % num == 0:
   num_line = int(length/num)
else:
   num_line = int(length/num)+1

for i in range(num_line):
   file_name = "hightemp_16_{}.txt".format(i)

   with open(file_name, "w") as fw:
      fw.write("\n".join(line_list[num*i:num*(i+1)]))
