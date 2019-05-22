# -*- coding: utf-8 -*-
# mecab neko.txt > neko.txt.mecab

import MeCab

NEKO_PATH = "./input/neko.txt"
OUTPUT_PATH = "./neko.txt.mecab"

f = open(NEKO_PATH)
neko_sentence = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

t = MeCab.Tagger('')

with open(OUTPUT_PATH, mode='w') as fw:
    fw.write(t.parse(neko_sentence))
