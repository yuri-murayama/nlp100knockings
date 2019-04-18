def cipher(sen):
    res = []
    result = ''

    for i in range(len(sen)):
        if sen[i].islower():
            res.append(chr(219-ord(sen[i])))
        else:
            res.append(sen[i])

    for i in res:
        result+=i
    
    print(result)

if __name__=='__main__':
    cipher("I am Kaei Cho.")
    cipher("I zn Kzvr Csl.")
