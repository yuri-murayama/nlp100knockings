with open('hightemp.txt', 'r' ) as f:
    N = int(input())
    l = f.readlines()
    for i in range(len(l)):
        if i % N != 0:
            print(l[i])
        else:
            print('-------------------------')
