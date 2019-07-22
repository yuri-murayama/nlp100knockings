import re
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

    def print(self):
        print(self.number)
        print([x.toList() for x in self.morphs])
        print(self.dst, self.srcs)
        print()

    def m_cut(self):
        seq = filter(lambda x: x.pos != '記号', self.morphs)
        return functools.reduce(lambda x, y: x + y.surface, seq, '')

class Pair:
    def __init__(self, particle, paragraph):
        self.particle = particle
        self.paragraph = paragraph

def analyze():
    article = []
    sentence = []
    chunk = None
    with open('neko.txt.cabocha', 'r', encoding='utf-8') as f:
        for line in f:
            words = re.split(r'\t|,|\n| ', line)
            if line[0] == '*':
                num = int(words[1])
                destNo = int(words[2].rstrip('D'))
                chunk = Chunk(num, destNo)
                sentence.append(chunk)
            elif words[0] == 'EOS':
                if sentence:
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

def f_non(sentence):
    for chunk in sentence:
        for m in chunk.morphs:
            if m.pos == '名詞':
                yield chunk
                break

def make_path(sentence, chunk):
    cl = sentence[chunk.number]
    list = []
    while cl.dst >= 0:
        list.append(cl.m_cut())
        cl = sentence[cl.dst]
    list.append(cl.m_cut())
    return list

def n_path(article):
    for sentence in article:
        for chunk in f_non(sentence):
            list = make_path(sentence, chunk)
            if len(list) >= 2:
                yield list

def main():
    article = analyze()
    with open('py48.txt', 'w', encoding='utf-8') as w:
        for list in n_path(article):
            w.write('{}\n'.format(
                ' -> '.join(list)
                )
                )

if __name__ == '__main__':
    main()
