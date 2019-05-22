# -*- coding: utf-8 -*-

from lesson36 import counterWord
import matplotlib.pyplot as plt

word_list = counterWord()
word_top10_list = word_list[:10]

left = range(0, 10)
height = [c for (w, c) in word_top10_list]
label = [w for (w, c) in word_top10_list]
plt.bar(left, height, tick_label=label, align="center")
plt.show()

"""
========
出力結果
========

[('の', 9194), ('。', 7486), ('て', 6848), ('、', 6772),
('は', 6420), ('に', 6243), ('を', 6071), ('だ', 5975),
('と', 5508), ('が', 5337) ...

"""
