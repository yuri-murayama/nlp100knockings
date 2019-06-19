#-*- coding: utf-8 -*-

def make_senlst(lines):
    sen_lst = []
    for line in lines:
        if len(line)>1: # 空白行ではないとき
            start = 0 # 文の開始インデックス
            for i in range(len(line)-2):
                if line[i] == ('.' or ';' or ':' or '?' or '!'):
                    if line[i+1] == ' ':
                        if line[i+2].isupper():
                            sen_lst.append(line[start:i+1])
                            start = i+2
            sen_lst.append(line[start:-1])
    
    return sen_lst


if __name__=='__main__':
    with open("nlp.txt") as f:
        lines = f.readlines() # 改行あり
    
    lst = make_senlst(lines)

    for l in lst:
        print(l)