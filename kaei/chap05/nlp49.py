#-*- coding: utf-8 -*-
import nlp40
import nlp41

# idの次から根までのpath
def make_path(id, sentence):
    path_lst = []
    dst = sentence[int(id)].dst
    while dst!='-1':
        path_lst.append(int(dst))
        dst = sentence[int(dst)].dst
    return path_lst

# id番目の文節の文字列を返す
def return_chunk(id, sentence, mode):
    chunk_frame = []
    if mode==True:
        for morph in sentence[int(id)].morphs:
            if morph.pos1!='句点' and morph.pos1!='読点':
                chunk_frame.append(morph.surface)
    else:
        flag=0
        for morph in sentence[int(id)].morphs:
            if morph.pos=='名詞':
                if flag==0:
                    chunk_frame.append(mode)
                    flag=1
            elif morph.pos1!='句点' and morph.pos1!='読点':
                chunk_frame.append(morph.surface)
    return "".join(chunk_frame)

def noun_to_noun(sentence):
    noun_chunk_id_lst = [] # 名詞を含む文節のインデックスリスト
    for i, chunk in enumerate(sentence):
        for morph in chunk.morphs:
            if morph.pos == '名詞':
                noun_chunk_id_lst.append(i)
                break
    
    for i, id_x in enumerate(noun_chunk_id_lst[:-1]):
        path_x = make_path(id_x, sentence)

        for id_y in noun_chunk_id_lst[i+1:]:
            # XからYに直結の時
            if id_y in path_x:
                id_end = path_x.index(id_y)
                print(return_chunk(id_x, sentence, 'X'), end="")

                for p in path_x[:id_end]:
                    print(' -> ', end="")
                    print(return_chunk(p, sentence, True), end="")
                print(' -> Y')

            # 経由する時
            else:
                path_y = make_path(id_y, sentence)
                for j, p in enumerate(path_y):
                    if p in path_x:
                        print(return_chunk(id_x, sentence, 'X'), end="")

                        k = path_x.index(p)
                        for pp in path_x[:k]:
                            print(' -> ', end="")
                            print(return_chunk(pp, sentence, True), end="")

                        print(' | ', end="")
                        print(return_chunk(id_y, sentence, 'Y'), end="")

                        for pp in path_y[:j]:
                            print(' -> ', end="")
                            print(return_chunk(pp, sentence, True), end="")
                        
                        print(' | ', end="")
                        print(return_chunk(p, sentence, True))

                        break


    print()
                    
                


if __name__=='__main__':
    with open("neko.txt.cabocha", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    lst = nlp41.make_chunk(lines)

    for sen in lst:
        noun_to_noun(sen)