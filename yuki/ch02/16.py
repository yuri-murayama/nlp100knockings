with open('hightemp.txt', 'r' ) as f:
    N = int(input())
    l = f.readlines()
    for i in range(len(l)):
        if i % N != 0:
            print(l[i])
        else:
            print('-------------------------')

#split -l 分割数 hightemp.txt
#これを実行するとファイルが分割されて新しいファイルができている
