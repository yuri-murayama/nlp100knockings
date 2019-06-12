from prob40 import Morph

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = []

    def __str__(self):
        surface_lst = [morph.surface for morph in self.morphs]
        return '{0} 係り先:{1}'.format(''.join(surface_lst), self.dst)

def load_neko():
    with open('neko.txt.cabocha') as f:
        lines = f.readlines()

    text = []
    sentence = []
    chunk = Chunk()

    for line in lines:
        if line.startswith('*'):
            if len(chunk.morphs) > 0:
                sentence.append(chunk)
                chunk = Chunk()
            l = line.split()
            chunk.dst = int(l[2].strip('D')) # 係り先を代入
        elif line == 'EOS\n':
            if len(chunk.morphs) > 0:
                sentence.append(chunk)
                chunk = Chunk()
            for i, c in enumerate(sentence):
                if c.dst != -1:
                    sentence[c.dst].srcs.append(i) # 係り元を代入
            text.append(sentence)
            sentence = []
        else:
            l = line.split('\t')
            ll = l[1].split(',')
            morph = Morph(
                surface=l[0],
                base=ll[6],
                pos=ll[0],
                pos1=ll[1]
            )
            chunk.morphs.append(morph)

    return text

if __name__ == '__main__':
    text = load_neko()
    for i, chunk in enumerate(text[7]):
        print(i, chunk)