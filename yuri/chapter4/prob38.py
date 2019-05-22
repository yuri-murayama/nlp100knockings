from prob30 import load_neko
from prob36 import count
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

text = load_neko()
dic = count(text)
count_lst = [d[1] for d in dic]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(count_lst, range=(0, 100), bins=20)
plt.title('単語の出現頻度のヒストグラム')
plt.xlabel('出現頻度')
plt.ylabel('単語の種類数')
plt.savefig('histogram.png')
plt.show()