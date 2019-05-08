import sys
with open('hightemp.txt', 'r') as f:
    l = f.readlines()
    args = sys.argv
    c = len(l)
    for i in range(int(args[1])):
        print(l[c-i-1],end = "")

#tail -n 4 hightemp.txt
