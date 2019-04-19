def cipher(s):
    s = [chr(219 - ord(c)) if c.islower() else c for c in s]
    return ''.join(s)
    
s = 'Hello Python'
encode = cipher(s)
print(encode)
decode = cipher(encode)
print(decode)

