# -*- coding: utf-8 -*-

# UNIX
# tail -n <num> hightemp.txt > hightemp_15.txt

# 実行コマンド
# python lesson15.py <num>

import sys

args = sys.argv  # コマンドライン引数
num = int(args[1])

INPUT_FILE = "hightemp.txt"
OUTPUT_FILE = "hightemp_15.txt"

with open(INPUT_FILE) as f:
   line_list = f.read().split("\n")

with open(OUTPUT_FILE, "w") as fw:
   fw.write("\n".join(line_list[-num-1:]))
