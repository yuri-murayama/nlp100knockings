import sys
with open('hightemp.txt', 'r' ) as f:
    args = sys.argv
    lis = []
    l = f.readlines()
    n = int(args[1])
    for i in range(len(l)):
        if (i+1) % n == 0:
            lis.append(l[i])
            with open('split{0:02}.txt'.format(i), 'w') as f2:
                for j in range(len(lis)):
                    f2.write(lis[j])
                lis = []
        else:
            lis.append(l[i])
    if len(l) % n != 0:
        with open('splitlast.txt', 'w') as f2:
            for j in range(len(lis)):
                f2.write(lis[j])
            
#split -l 分割数 hightemp.txt
#これを実行するとファイルが分割されて新しいファイルができている
