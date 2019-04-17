# -*- coding: utf-8 -*-

s = "Now I need a drink, alcoholic of course, " \
    "after the heavy lectures involving quantum mechanics."
word_list = s.split(" ")
lengths = [len(w.strip(",")) for w in word_list]
print(lengths)
