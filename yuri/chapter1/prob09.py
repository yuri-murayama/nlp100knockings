import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
s = s.split()

lst = []
for w in s:
    if len(w) > 4:
        w_naka = list(w[1:-1])
        random.shuffle(w_naka)
        w_naka = ''.join(w_naka)
        w = w[0] + w_naka + w[-1]
    lst.append(w)

print(' '.join(lst))