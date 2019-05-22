# -*- coding: utf-8 -*-

from lesson36 import counterWord
import matplotlib.pyplot as plt
import math

word_list = counterWord()
word_counter = {}
for (w,c) in word_list:
    if c in word_counter:
        word_counter[c] += 1
    else:
        word_counter[c] = 1

# そーと
score_sorted = sorted(word_counter.items(), key=lambda x:x[0])
print(score_sorted)
left = []
height = []
for i, (k,v) in enumerate(score_sorted):
    left.append(i)
    height.append(math.log(v))
#print(height)
plt.bar(left, height)
plt.show()

"""
========
出力結果
========
[8.458504195067558, 7.552762084214147, 6.863803391452954,
6.401917196727186, 6.129050210060545, 5.780743515792329,
5.484796933490655, ...

"""
