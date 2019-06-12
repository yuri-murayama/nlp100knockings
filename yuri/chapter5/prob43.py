from prob41 import load_neko

def contain_pos(chunk, pos_name):
    booll = False
    for morph in chunk.morphs:
        if morph.pos == pos_name:
            booll = True
    return booll

def depend2(sentence):
    lst = []
    for chunk in sentence:
        if contain_pos(chunk, '名詞') and contain_pos(sentence[chunk.dst], '動詞'):
            from_surface = ''.join([morph.surface.strip('。') for morph in chunk.morphs])
            to_surface = ''.join([morph.surface.strip('。') for morph in sentence[chunk.dst].morphs])
            lst.append((from_surface, to_surface))
    return lst


if __name__ == '__main__':
    text = load_neko()
    for t in depend2(text[7]):
        print(t[0], '\t', t[1])