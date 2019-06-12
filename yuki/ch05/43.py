import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = []

    def __str__(self):
        surface_lst = [morph.surface for morph in self.morphs]
        return '{0} 係り先:{1}'.format(''.join(surface_lst),self.dst)

def judge(chunk,pos):
    boolian = False
    for morph in chunk.morphs:
        if morph.pos == pos:
            boolian =True
    return boolian

def print_bunnsetsu(sentence):
    surface_dic = {}
    lst = []
    for i, chunk in enumerate(sentence):
        surface_lst = []
        surface_lst = [morph.surface.rstrip("。、") for morph in chunk.morphs]
        surface_dic[i]  = surface_lst
    for i, chunk in enumerate(sentence):
        if chunk.dst != -1:
            if judge(chunk,'名詞') and judge(sentence[chunk.dst],'動詞'):
                lst.append((''.join(surface_dic[i]),''.join(surface_dic[chunk.dst])))
    return lst

def chunk_list():
    text = [] #文章の形態素解析が格納されている　１文が一つのリスト
    sentence = []
    chunk = Chunk()
    with open('neko.txt.cabocha','r') as f:
        lines = f.readlines()  #read()だと１文字ずつ読み込んでしまう
        for line in lines:
            split_line = re.split(',|\t|\n|\s',line)
            if split_line[0] == '*':
                if len(chunk.morphs) > 0:
                    sentence.append(chunk)
                    chunk = Chunk()
                chunk.dst = int(split_line[2].rstrip("D"))
            elif split_line[0] == 'EOS':
                if len(chunk.morphs) > 0:
                    sentence.append(chunk)
                    chunk = Chunk()
                for i, c in  enumerate(sentence):
                    if c.dst != -1:
                        sentence[c.dst].srcs.append(i)
                text.append(sentence)
                sentence = [] #sentenceの初期化
            else:
                chunk.morphs.append(Morph(split_line[0],split_line[7],split_line[1],split_line[2]))
    return text

if __name__ =='__main__':
    text = chunk_list()
    for sentence in text:
        lst = print_bunnsetsu(sentence)
        if len(lst) > 0:
            for i in range(len(lst)):
                print(lst[i][0]+'\t'+lst[i][1])
            print()
