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


def f_verb(sentence):
    for chunk in sentence:
        for m in reversed(chunk.morphs):
            if m.pos == '動詞':
                yield m, chunk.number
                break

def f_post(sentence, number):
    for chunk in sentence:
        if chunk.dst == number:
            n_morph = Morph('', '', '', '')
            for m in reversed(chunk.morphs):
                if n_morph.pos == '助詞':
                    yield m, n_morph, chunk.m_cut()
                    break
                n_morph = m

def uni(article):
    for sentence in article:
        for v, num in f_verb(sentence):
            list1 = []
            object = ''
            for p1, p2, q in f_post(sentence, num):
                if p1.pos == '名詞' and p1.pos1 == 'サ変接続' and p2.surface == 'を':
                    object = p1.surface + p2.surface
                else:
                    list1.append(Pair(p2.surface, q))
            if list1 and object != '':
                yield object + v.base, sorted(list1, key=lambda x: x.particle)

def main():
    article = analyze()
    with open('py47.txt', 'w', encoding='utf-8') as w:
        for v, list1 in uni(article):
            w.write('{}\t{}\t{}\n'.format(
                v,
                ' '.join([x.particle for x in list1]),
                ' '.join([x.paragraph for x in list1]
                )
                )
                )

if __name__ == '__main__':
    main()
