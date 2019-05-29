#-*- coding: utf-8 -*-

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    # print用メソッド
    def print_obj(self):
        print("surface : {0}, base : {1}, pos : {2}, pos1 : {3}".format(self.surface, self.base, self.pos, self.pos1))

def make_lst():
    with open("neko.txt.cabocha", 'r', encoding="utf-8") as f:
        lines = f.readlines()

    lst = []
    sen_lst = []

    for line in lines:
        # 文末
        if line=='EOS\n':
            if len(sen_lst)>0:
                lst.append(sen_lst)
            sen_lst = []
        
        else:
            line = line.strip().split('\t')
            if line[-1]=='O':
                # 空白のとき
                if len(line)==2:
                    surface = ' '
                else:
                    surface = line[0]

                l = line[-2].split(',')
                word = Morph(surface, l[6], l[0], l[1])
                sen_lst.append(word)
    return lst

if __name__=='__main__':
    lst = make_lst()
    
    for i in lst[3]:
        i.print_obj()
