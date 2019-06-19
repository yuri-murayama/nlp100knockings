import re

class Morph: #[表層形,基本型,品詞,品詞細分類1]
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk: #[Morph,係り先文節のインデックス,係り元文節のインデックス]
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = []

    def __str__(self):
        surface_lst = [morph.surface for morph in self.morphs]
        return '{0} 係り先:{1}'.format(''.join(surface_lst),self.dst)

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

def judge(chunk,pos):
    boolian = False
    for morph in chunk.morphs:
        if morph.pos == pos:
            boolian =True
    return boolian

def search_particle(chunk):
    for morph in chunk.morphs:
        if morph.pos == '助詞':
            particle_base = morph.base
    return particle_base

def search_verb(chunk):
    for morph in chunk.morphs:
        if morph.pos == '動詞':
            return morph.base

def verb_case_pattern_extraction(sentence):
    verb_particle_pair = []
    for chunk in sentence: #文の中から１文節ずつ動詞を探す
            if judge(chunk,'動詞'):
                particle_list = []
                for kakarimoto_index in chunk.srcs: #動詞が見つかり文節の係り元リストの要素数だけループ
                    if judge(sentence[kakarimoto_index],'助詞'):
                        particle_list.append(search_particle(sentence[kakarimoto_index]))
                if len(particle_list) > 0:
                    verb = search_verb(chunk)
                    verb_particle_pair.append([verb,' '.join(particle_list)])
    return verb_particle_pair

if __name__ =='__main__':
    text = chunk_list()
    for sentence in text:
        verb_particle_pair = verb_case_pattern_extraction(sentence)
        for p in verb_particle_pair:
            print(p[0]+'\t'+p[1])
