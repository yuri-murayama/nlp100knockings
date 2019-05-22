from prob30 import load_neko
from prob36 import count
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

text = load_neko()
dic = count(text)
rank_lst = [i+1 for i in range(len(dic))]
count_lst = [d[1] for d in dic]

x = rank_lst
y = count_lst
plt.plot(x,y)
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.set_yscale('log')
ax.set_xscale('log')
plt.title('Zipfの法則')
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.show()
plt.savefig('zipfs-law.png')