# -*- coding: utf-8 -*-     

def cipher(s):
    t = ""
    for w in s:
        if w.islower():
            w = chr(219 - ord(w))
            t += w
        else:
            t += w
    return t

st = "MoZi ReTsu!"

print(cipher(st))
print(cipher(cipher(st)))
