with open('col1.txt','r') as col1:
    with open('col2.txt', 'r') as col2:
        with open('marge.txt','w') as m:
            col1 = list(col1)
            col2 = list(col2)
            for i in range(len(col1)):
                m.write(col1[i][:-1:]+'\t'+col2[i])

#paste col1.txt col2.txt
