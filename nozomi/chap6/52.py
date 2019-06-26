# -*- coding: utf-8 -*-

import re
from nltk.stem import PorterStemmer

with open('output51.txt','r') as f:
    ps = PorterStemmer()
    for l in f:
        l=l.strip('\n')
        print(l,'\t', ps.stem(l))
        #print()
