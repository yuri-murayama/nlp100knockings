with open('hightemp.txt', 'r') as f:
    with open('hightemp2.txt', 'w') as f2: 
        for line in f:
            line2 = line.replace('\t',' ')
            f2.write(line2)

#expand hightemp.txt
