#-*- coding: utf-8 -*-

import nlp40

class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

def make_chunk():
    with open("neko.txt.cabocha", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lst = []
    class_lst = []
    sen_lst = []
    chunk_lst = []
    srcs_dic = {}
    dst_lst = []

    for line in lines:
        # 文末
        if line=='EOS\n':
            if len(chunk_lst)>0:
                sen_lst.append(chunk_lst)

            chunk_lst = []

            if len(sen_lst)>0:
                for i, ch in enumerate(sen_lst):
                    key = str(i) + 'D'
                    if key in srcs_dic:
                        srcs = srcs_dic[key]
                    else:
                        srcs = []

                    chunk = Chunk(ch, dst_lst[i], srcs)
                    class_lst.append(chunk)

                lst.append(class_lst)
            class_lst = []
            sen_lst = []
            srcs_dic = {}
            dst_lst = []
            
        else:
            if line[0]=='*':
                if len(chunk_lst)>0:
                    sen_lst.append(chunk_lst)
                
                chunk_lst = []

                # 係り元情報の記憶
                l = line.strip().split(' ')
                if l[2] in srcs_dic.keys():
                    srcs_dic[l[2]] = srcs_dic[l[2]]+[l[1]]
                else:
                    srcs_dic[l[2]] = [l[1]]
                
                dst_lst.append(l[2][:-1])
                
            else:
                line = line.strip().split('\t')
                # 空白のとき
                if len(line)==2:
                    surface = ' '
                else:
                    surface = line[0]

                l = line[-2].split(',')
                word = nlp40.Morph(surface, l[6], l[0], l[1])
                chunk_lst.append(word)

    return lst

if __name__=='__main__':
    lst = make_chunk()

    for chunk in lst[7]:
        morphs = chunk.morphs
        dst = chunk.dst
        print("morphs : ",end="")
        for morph in morphs:
            print(morph.surface, end="")
        print("")
        print("dst : " + dst)
        print("srcs : ", end="")
        print(chunk.srcs)
        print("")
