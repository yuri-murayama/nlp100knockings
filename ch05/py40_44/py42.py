import re
import functools

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def m_list(self):
        return [self.surface, self.base, self.pos, self.pos1]


class Chunk:
    def __init__(self, number, dst):
        self.number = number
        self.morph = []
        self.dst = dst
        self.srcs = []

    def print(self):
        print(self.number)
        print([x.m_list() for x in self.morph])
        print(self.dst, self.srcs)
        print()
    
    def m_cut(self):
        seq = filter(lambda x: x.pos != '記号', self.morph)
        return functools.reduce(lambda x, y: x + y.surface, seq, '')


def analyze():
    article = []
    sentence = []
    chunk = None

    with open('neko.txt.cabocha', 'r', encoding='utf8') as f:
        for line in f:
            words = re.split(r'\t|\n|,| ', line)
            if line[0] == '*':
                num = int(words[1])
                dest_num = int(words[2].rstrip("D"))
                chunk = Chunk(num, dest_num)
                sentence.append(chunk)
            elif words[0] == 'EOS':
                if sentence:
                    for idx, c in enumerate(sentence, 0):
                        sentence[c.dst].srcs.append(idx)
                    article.append(sentence)
                sentence = []
            else:
                chunk.morph.append(Morph(
                    words[0],
                    words[7],
                    words[1],
                    words[2]
                )
                )
    return article

def print_tab(wr, sentence):
    for chunk in sentence:
        if chunk.dst == -1:
            continue
        s = chunk.m_cut()
        if s != '':
            t = sentence[chunk.dst].m_cut()
            wr.write("{s}\t{t}\n".format(s=s, t=t))

def main():
    article = analyze()
    with open('py42.txt', 'w', encoding='utf8') as w:
        for sentence in article:
            print_tab(w, sentence)

if __name__ == "__main__":
    main()
