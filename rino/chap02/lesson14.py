# -*- coding: utf-8 -*-

# UNIX
# head -n <num> hightemp.txt > hightemp_14.txt

# 実行コマンド
# python lesson14.py <num>

import sys

args = sys.argv  # コマンドライン引数
num = int(args[1])

INPUT_FILE = "hightemp.txt"
OUTPUT_FILE = "hightemp_14.txt"

with open(INPUT_FILE) as f:
   line_list = f.read().split("\n")

with open(OUTPUT_FILE, "w") as fw:
   fw.write("\n".join(line_list[:num]))
