from prob41 import load_neko
from prob43 import contain_pos

def noun2root(sentence):
    lst = []
    for chunk in sentence:
        if contain_pos(chunk, '名詞'):
            path_lst = []
            start = ''.join([morph.surface.strip('。、') for morph in chunk.morphs])
            path_lst.append(start)
            while chunk.dst != -1:
                end = ''.join([morph.surface.strip('。、') for morph in sentence[chunk.dst].morphs])
                path_lst.append(end)
                chunk = sentence[chunk.dst]
            lst.append(path_lst)
    return lst

if __name__ == '__main__':
    text = load_neko()
    for l in noun2root(text[7]):
        print(' -> '.join(l))