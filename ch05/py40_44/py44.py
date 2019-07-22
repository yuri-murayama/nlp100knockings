import re
import functools
import pydot

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

def contains(chunk, pos):
    return any(m.pos == pos for m in chunk.morph)

def ntov(article):
    for sentence in article:
        for chunk in sentence:
            if chunk.dst >= 0 and contains(chunk, '名詞'):
                target = sentence[chunk.dst]
                if contains(target, '動詞'):
                    yield chunk, target


def print_tab(wr, noun, verb):
    s = noun.m_cut()
    if s != '':
        t = verb.m_cut()
        wr.write("{}\t{}\n".format(s, t))

def dot(sentence):
    edges = []
    for chunk in sentence:
        if chunk.dst >= 0:
            edges.append(
                (chunk.m_cut(), sentence[chunk.dst].m_cut()))
    return edges


def main():
    graph = pydot.Dot(graph_type='digraph')
    graph.set_node_defaults(fontname='AppleGothic', fontsize='12')

    article = analyze()
    for s, t in dot(article[4]):
        graph.add_edge(pydot.Edge(s, t))
    graph.write_png('py44.png')


if __name__ == "__main__":
    main()
