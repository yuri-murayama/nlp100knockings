import re
import sys
import copy
import functools

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def toList(self):
        return [self.surface, self.base, self.pos, self.pos1]

class Chunk:
    def __init__(self, number, dst):
        self.number = number
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def Noun(self):
        for m in self.morphs:
            if m.pos == '名詞':
                return True
        return False

    def print(self):
        print(self.number)
        print([x.toList() for x in self.morphs])
        print(self.dst, self.srcs)
        print()

    def m_cut(self):
        seq = filter(lambda x: x.pos != '記号', self.morphs)
        return functools.reduce(lambda x, y: x + y.surface, seq, '')


def analyze():
    article = []
    sentence = []
    chunk = None
    with open('neko.txt.cabocha', 'r', encoding='utf-8') as fin:
        for line in fin:
            words = re.split(r'\t|,|\n| ', line)
            if line[0] == '*':
                num = int(words[1])
                destNo = int(words[2].rstrip('D'))
                if destNo == -1:
                    destNo = num + 1
                chunk = Chunk(num, destNo)
                sentence.append(chunk)
            elif words[0] == 'EOS':
                if sentence:
                    sentence.append(Chunk(sys.maxsize, -1))
                    for index, c in enumerate(sentence, 0):
                        sentence[c.dst].srcs.append(index)
                    article.append(sentence)
                sentence = []
            else:
                chunk.morphs.append(Morph(
                    words[0],
                    words[7],
                    words[1],
                    words[2],
                ))
    return article

def noun_pair(sentence):
    count = len(sentence)
    for i in range(count):
        for j in range(i+1, count):
            if sentence[i].Noun() and sentence[j].Noun():
                yield sentence[i], sentence[j]

def contain(c_i, c_j, sentence):
    c2 = c_i
    while c2.dst >= 0:
        if c2 == c_j:
            return True
        c2 = sentence[c2.dst]
    return False

def connect(c_i, c_j, sentence):
    k = c_i.dst
    while k >= 0:
        c3 = c_j
        while c3.dst >= 0:
            if c3.number == k:
                return k
            c3 = sentence[c3.dst]
        k = sentence[k].dst
    return -1

def replace(to, chunk):
    x = copy.deepcopy(chunk)
    for m in x.morphs:
        if m.pos == '名詞':
            m.surface = to
            break
    return x

def make1(c_i, c_j, sentence):
    path = []
    y = replace('X', c_i)
    while y.number < c_j.number:
        path.append(y.m_cut())
        y = sentence[y.dst]
    path.append('Y')
    return '{}'.format(
    ' -> '.join(path)
    )

def make2(c_i, c_j, c_k, sentence):
    c_i = replace('X', c_i)
    c_j = replace('Y', c_j)
    p1 = c_i.m_cut()
    list1 = []
    z = c_j
    while z.number < c_k.number:
        list1.append(z.m_cut())
        z = sentence[z.dst]
    p2 = '{}'.format(' -> '.join(list1))
    list2 = []
    z = c_k
    while z.dst > 0:
        list2.append(z.m_cut())
        z = sentence[z.dst]
    p3 = '{}'.format(' -> '.join(list2))
    return '{} | {} | {}'.format(p1, p2, p3)

def otherpath(sentence):
    for c_i, c_j in noun_pair(sentence):
        if contain(c_i, c_j, sentence):
            yield make1(c_i, c_j, sentence)
        else:
            k = connect(c_i, c_j, sentence)
            if k > 0:
                yield make2(c_i, c_j, sentence[k], sentence)

def main():
    article = analyze()
    with open('py49.txt', 'w', encoding='utf-8') as w:
        for sentence in article:
            for path in otherpath(sentence):
                w.write(path + '\n')

if __name__ == '__main__':
    main()
