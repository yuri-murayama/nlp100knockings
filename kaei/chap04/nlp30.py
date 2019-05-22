#-*- coding: utf-8 -*-

def make_lst():
    with open("neko.txt.mecab", "r",encoding="utf-8") as f:
        lines = f.readlines()

    lst = []
    sen_lst = []

    for line in lines:
        line = line.strip().split("\t")
        if len(line)==1:
            l = line[0].split(",")
            if len(l)>1:
                dic = {"surface":"　", "base":l[6], "pos":l[0], "pos1":l[1]}
                sen_lst.append(dic)

        if len(line)==2:
            l = line[1].split(",")
            
            dic = {"surface":line[0], "base":l[6], "pos":l[0], "pos1":l[1]}
            sen_lst.append(dic)

            if l[1] == "句点":
                lst.append(sen_lst)
                sen_lst = []
    return lst

if __name__=='__main__':
    lst = make_lst()
    print(lst[5])
    
