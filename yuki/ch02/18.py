with open('hightemp.txt', 'r') as f:
    with open('sort.txt', 'w') as s:
        l = f.readlines()
        lines = sorted(l, key=lambda x: x.split()[2], reverse = True)
        for i in lines:
            s.write(i)
    