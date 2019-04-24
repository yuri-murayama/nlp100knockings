with open('col1.txt','r') as col1:
    l = col1.readlines()
    col = list(set(l))
    print(len(col))
