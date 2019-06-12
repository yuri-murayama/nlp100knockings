from prob41 import load_neko

def depend(sentence):
    lst = []
    for chunk in sentence:
        if chunk.dst != -1:
            from_surface = ''.join([morph.surface.strip('。') for morph in chunk.morphs])
            to_surface = ''.join([morph.surface.strip('。') for morph in sentence[chunk.dst].morphs])
            lst.append((from_surface, to_surface))
    return lst


if __name__ == '__main__':
    text = load_neko()
    for t in depend(text[7]):
        print(t[0], '\t', t[1])