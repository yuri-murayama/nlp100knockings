# -*- coding: utf-8 -*-
import random

s = "I couldn't believe that " \
    "I could actually understand what I was reading : " \
    "the phenomenal power of the human mind ."
word_list = s.split(" ")

new_list = []
for w in word_list:
    length_word = len(w)
    if length_word > 4:
        random_word = w[0]
        random_word += ''.join(random.sample(w[1:-1], length_word-2)) # 並び替え処理
        random_word += w[length_word-1]
        new_list.append(random_word)
    else:
        new_list.append(w)

new_text = " ".join(new_list)
print(new_text)
