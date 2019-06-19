from prob41 import load_neko
from prob43 import contain_pos
from prob45 import get_left_morph, get_right_morph 

def get_case_frame(sentence):
    lst = []
    for chunk in sentence:
        if contain_pos(chunk, '動詞'):
            plst = []
            clst = []
            for i in chunk.srcs:
                if contain_pos(sentence[i], '助詞'):
                    plst.append(get_right_morph(sentence[i], '助詞'))
                    clst.append(''.join([morph.surface.strip('。、') for morph in sentence[i].morphs]))
            if len(plst) > 0:
                lst.append((get_left_morph(chunk, '動詞'), ' '.join(plst), ' '.join(clst)))
    return lst

if __name__ == '__main__':
    text = load_neko()
    with open('case_frame.txt', 'w', encoding='utf-8') as f:
        for sentence in text:
            for t in get_case_frame(sentence):
                f.write(t[0] + '\t' + t[1] + '\t' + t[2] + '\n')