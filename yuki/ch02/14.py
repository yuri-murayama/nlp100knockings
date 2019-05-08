with open('hightemp.txt', 'r') as f:
    N = int(input())
    l = f.readlines()
    for i in range(N):
        print(l[i])
#head -n 行数 hightemp.txt

