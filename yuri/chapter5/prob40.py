class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface:{0}, base:{1}, pos:{2}, pos1:{3}'.format(self.surface, self.base, self.pos, self.pos1)

def load_neko():
    with open('neko.txt.cabocha') as f:
        lines = f.readlines()

    text = []
    sentence = []

    for line in lines:
        if line.startswith('*'):
            pass
        elif line == 'EOS\n':
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
            sentence.append(morph)

    return text

if __name__ == '__main__':
    text = load_neko()
    for morph in text[2]:
        print(morph)