# -*- coding: utf-8 -*-

from lesson05 import createCharNgram

s1 = "paraparaparadise"
x = createCharNgram(s1, 2)
print("x:{}".format(x))

s2 = "paragraph"
y = createCharNgram(s2, 2)
print("y:{}".format(y))

# 和集合
and_not_uniqu = []
for t in x:
    if t in y:
        and_not_uniqu.append(t)
s1_s2_and = list(set(and_not_uniqu))
print("和集合:{}".format(s1_s2_and))


# 積集合
s1_s2_prod = []
sum_list = x + y
for t in sum_list:
    if t not in s1_s2_prod:
        s1_s2_prod.append(t)
print("積集合:{}".format(s1_s2_prod))


# 差集合
s1_s2_diff = []
for t in x:
    if t not in y:
        s1_s2_diff.append(t)
print("差集合:{}".format(s1_s2_diff))

# se in x?
if "se" in x:
    print("x has se")
else:
    print("x doesn't has se")

# se in y?
if "se" in y:
    print("y has se")
else:
    print("y doesn't has se")
