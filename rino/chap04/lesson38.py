# -*- coding: utf-8 -*-

from lesson36 import counterWord
import matplotlib.pyplot as plt

word_list = counterWord()
word_counter = {}
for (w,c) in word_list:
    if c in word_counter:
        word_counter[c] += 1
    else:
        word_counter[c] = 1

# そーと
score_sorted = sorted(word_counter.items(), key=lambda x:x[0])
height = []
for k,v in score_sorted:
    height.append(v)
plt.hist(height, bins=50)
plt.show()

"""
========
出力結果
========
[(1, 4715), (2, 1906), (3, 957), (4, 603), (5, 459),
(6, 324), (7, 241), (8, 207), (9, 159), (10, 125), (11, 120),...

"""
