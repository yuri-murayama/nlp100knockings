def make_gram(str, type):
    result = []
    if type=="word":
        str = str.split()

        for i in range(1, len(str)):
            result.append(str[i-1]+" "+str[i])

    elif type=="chara":
        str = str.replace(" ", "")

        for i in range(1, len(str)):
            result.append(str[i-1]+str[i])

    return result

if __name__ == '__main__':
    str = "I am an NLPer"
    print(make_gram(str, "word"))
    print(make_gram(str, "chara"))
