# -*- coding: utf-8 -*-     

import random

def shuf_w(w):
 if len(w) > 4:
  rndm = list(w[1:-1])
  random.shuffle(rndm)
  return w[0] + "".join(rndm) + w[-1] 
 else:
  return w

def shuf(x):   
 return " ".join(list(map(shuf_w,x.split())))

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(shuf(s))

