import nlp05

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(nlp05.make_gram(str1, "chara"))
Y = set(nlp05.make_gram(str2, "chara"))

# 和集合
print(X | Y)

# 積集合
print(X & Y)

# 差集合
print(X - Y)

# "se"がXおよびYに含まれるかどうか
if "se" in X or "se" in Y:
    print("TRUE")

