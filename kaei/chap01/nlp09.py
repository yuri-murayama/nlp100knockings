import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

str = str.split()
result = []

for i in str:
    if len(i)>4:
        word = list(i[1:-1]).copy()
        random.shuffle(word)
        word = ''.join(word)
        result.append(i[0]+word+i[-1])
    else:
        result.append(i)

print(' '.join(result))
