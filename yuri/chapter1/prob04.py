s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
number_lst = [1, 5, 6, 7, 8, 9, 15, 16, 19]

s = s.strip('.').split()

dic = {}
i = 1
for w in s:
    if i in number_lst:
        dic[w[0]] = i
    else:
        dic[w[:2]] = i
    i += 1

dic = sorted(dic.items(), key=lambda x: x[1])
print(dic)


