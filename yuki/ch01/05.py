def ngram(n, str):
    word = str.split(" ")
    char = str.replace(" ","")
    print('単語')
    for i in range(len(word)-1):
        for j in range(n):
            if j!= n-1:
                print(word[j+i], end=' ')
            else:
                print(word[j+i])

    print('文字')
    for i in range(len(char)-1):
        for j in range(n):
            if j!= n-1:
                print(char[j+i],end = '')
            else:
                print(char[j+i])
                
    return
        
if __name__ == "__main__":
    print('nを入力')
    n = int(input())
    print('文字列入力')
    str = input()
    ngram(n,str)
