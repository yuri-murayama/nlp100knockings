import random

lines_pos = []
lines_neg = []

with open('./rt-polaritydata/rt-polarity.pos','r', encoding='cp1252') as p:
    for line in p:
        lines_pos.append('+1 ' + line)
    text1 = lines_pos

with open('./rt-polaritydata/rt-polarity.neg','r', encoding='cp1252') as n:
    for line in n:
        lines_neg.append('-1 ' + line)
    text2 = lines_neg

text3 = text1 + text2
random.shuffle(text3)

with open('sentiment.txt', 'w') as f:
    f.writelines(text3)
