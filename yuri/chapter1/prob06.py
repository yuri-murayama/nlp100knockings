def n_gram(s, n):
    return [s[i:i+n] for i in range(len(s)-1)]

s1 = "paraparaparadise"
s2 = "paragraph"

X = set(n_gram(s1, 2))
Y = set(n_gram(s2, 2))

union = X.union(Y)
intersection = X.intersection(Y)
difference = X.difference(Y)

print('和集合: {}'.format(union))
print('積集合: {}'.format(intersection))
print('差集合: {}'.format(difference))

print('se' in X)
print('se' in Y)

