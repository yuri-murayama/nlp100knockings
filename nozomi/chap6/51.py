# -*- coding: utf-8 -*-

import re

with open('output50.txt','r') as f:
    for l in f:
        l=l.strip('\n')
        m=re.sub(r'(\s)(.)', r'\1\n\2',l, flags=re.MULTILINE)
        print(m)
        print()
