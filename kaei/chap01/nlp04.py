str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str = str.split()
dic = {}

for key, value in enumerate(str):
    if key in [0,4,5,6,7,8,14,15,18]:
        dic[key] = value[0]
    else:
        dic[key] = value[:2]

print(dic)
        
