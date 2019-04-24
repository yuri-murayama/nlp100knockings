with open('hightemp.txt', 'r') as f:
    l = f.readlines()
    c = len(l)
    N = int(input())
    for i in range(N):
        print(l[c-i-1])
