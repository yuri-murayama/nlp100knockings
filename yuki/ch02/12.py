with open('hightemp2.txt','r') as f:
    with open('col1.txt','w') as col1:
        with open('col2.txt','w') as col2:
            for line in f:
                line2 = line.split(' ')
                col1.write(line2[0]+'\n')
                col2.write(line2[1]+'\n')
            
