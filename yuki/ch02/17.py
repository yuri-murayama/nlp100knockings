with open('col1.txt','r') as col1:
    l = col1.readlines()
    col = list(set(l))
    print(len(col))

#cat hightemp.txt | cup -f | sort | uniq
#uniqは連続して重複している行を連続しないようにする、そのためsortしてからuniqすると全ての重複がなくなることになる
