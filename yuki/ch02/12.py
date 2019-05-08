with open('hightemp2.txt','r') as f:
    with open('col1.txt','w') as col1:
        with open('col2.txt','w') as col2:
            for line in f:
                line2 = line.split(' ')
                col1.write(line2[0]+'\n')
                col2.write(line2[1]+'\n')
            
#cat ./hightemp.txt | cut -f 1 この場合の1は1項目目を表す.つまり１番左の列
#もしくは cut -f 1 hightemp.txt 
#cat ./hightemp.txt | cut -f 2
#もしくは cut -f 2 hightemp.txt
#もし1行目と2行目を取り出したければ cat -f 1-2 hightemp.txt とする

