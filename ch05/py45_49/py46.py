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
        for m in chunk.morphs:
            if m.pos == '動詞':
                yield m, chunk.number
                break

def f_post(sentence, number):
    for chunk in sentence:
        if chunk.dst == number:
            for m in reversed(chunk.morphs):
                if m.pos == '助詞':
                    yield m, chunk.m_cut()
                    break

def uni(article):
    for sentence in article:
        for v, num in f_verb(sentence):
            list1 = []
            list2 = []
            for p, q in f_post(sentence, num):
                list1.append(p.surface)
                list2.append(q)
            if list1:
                yield v.base, sorted(list1, key=lambda x: x), sorted(list2, key=lambda x: x)

def main():
    article = analyze()
    with open('py46.txt', 'w', encoding='utf-8') as f2:
        for i, j, k in uni(article):
            f2.write('{}\t{}\t{}\n'.format(
                i,
                ' '.join(j),
                ' '.join(k)
                )
                )

if __name__ == '__main__':
    main()
