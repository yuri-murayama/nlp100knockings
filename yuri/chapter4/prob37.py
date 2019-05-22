from prob30 import load_neko
from prob36 import count
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

text = load_neko()
dic = count(text)
word_lst = [d[0] for d in dic]
count_lst = [d[1] for d in dic]

left = np.array([1,2,3,4,5,6,7,8,9,10])
height = np.array(count_lst[:10])
label = word_lst[:10]
plt.bar(left, height, tick_label=label)
plt.title('頻度上位10語')
plt.xlabel('単語')
plt.ylabel('出現頻度')
plt.show()
plt.savefig('frequency-top-10.png')