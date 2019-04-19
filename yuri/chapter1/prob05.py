def n_gram(s, n):
    return [s[i:i+n] for i in range(len(s)-1)]

s = "I am an NLPer"
print('文字bi-gram: {}'.format(n_gram(s, 2)))
s = s.split()
print('単語bi-gram: {}'.format(n_gram(s, 2)))
