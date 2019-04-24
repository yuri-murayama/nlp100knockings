str1 = 'paraparaparadise'
str2 = 'paragraph'
X = []
Y = []
Z = []
U = []
S = []
for i in range(len(str1)-1):
    X.append(str1[i]+str1[i+1])
print('Xの集合')
print(X)
for i in range(len(str2)-1):
    Y.append(str2[i]+str2[i+1])
print('Yの集合')
print(Y)

print('和集合')
for i in range(len(X)):
    if X[i] not in U:
        U.append(X[i])
for i in range(len(Y)):
    if Y[i] not in U:
        U.append(Y[i])
print(U)

print('積集合')
for i in range(len(X)):
    for j in range(len(Y)):
        if X[i] == Y[j] and X[i] not in Z:
            Z.append(X[i])
print(Z)

print('差集合')
for i in range(len(U)):
    if U[i] not in Z:
        S.append(U[i])
print(S)


if 'se' in X:
    print('seがXに含まれる')
else:
    print('seがXに含まれない')

if 'se' in Y:
    print('seがYに含まれる')
else:
    print('seがYに含まれない')
