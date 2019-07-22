import re

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def m_list(self):
        return [self.surface, self.base, self.pos, self.pos1]

class Chunk:
    def __init__(self,number,dst):
        self.number = number
        self.morph = []
        self.dst = dst
        self.srcs = []

    def print(self):
        print(self.number)
        print([x.m_list() for x in self.morph])
        print(self.dst, self.srcs)
        print()


def analyze():
    article = []
    sentence = []
    chunk = None

    with open('neko.txt.cabocha','r',encoding = 'utf8') as f:
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

def main():
    article = analyze()
    for c in article[8]:
        c.print()

if __name__ == "__main__":
    main()
