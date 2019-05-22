# -*- coding: utf-8 -*-

from lesson36 import counterWord
import matplotlib.pyplot as plt

word_list = counterWord()

left = []
height = []
for i, (k,v) in enumerate(word_list):
    left.append(i+1)
    height.append(v)

plt.xscale('log')
plt.yscale('log')
plt.plot(left, height)
plt.show()
