# -*- coding: utf-8 -*-

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
    "New Nations Might Also Sign Peace " \
    "Security Clause. Arthur King Can."
word_list = s.split(" ")
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]  # 先頭の1文字を取り出すindex
chemical_dict = {}

for num, w in enumerate(word_list, 1):
    if num in index:
        c = w[0]
    else:
        c = w[:2]
    chemical_dict[c] = num

print(chemical_dict)
