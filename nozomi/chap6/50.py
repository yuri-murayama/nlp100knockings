# -*- coding: utf-8 -*-

import re

with open('nlp.txt','r') as f:
    #m = re.match(r'(.+)[\.;:\?!])\s[A-Z](.*)')できなかった
    for l in f:
        l=l.strip('')
        m=re.sub(r'([\.;:\?!]\s)([A-Z])', r'\1\n\2',l, flags=re.MULTILINE)
        print(m)
