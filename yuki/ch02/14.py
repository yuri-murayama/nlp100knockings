import sys
with open('hightemp.txt', 'r') as f:
    args = sys.argv
    l = f.readlines()
    for i in range(int(args[1])):
        print(l[i],end = "")
#head -n 行数 hightemp.txt

