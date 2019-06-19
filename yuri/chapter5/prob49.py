from prob41 import load_neko
from prob43 import contain_pos
from prob48 import noun2root

def mask(clause, sentence, charac):
    masked_clause = ' '
    flag = 0
    for chunk in sentence:
        s = ''.join([morph.surface.strip('。、') for morph in chunk.morphs])
        if s == clause:
            for morph in chunk.morphs:
                if morph.pos == '名詞':
                    if flag == 0:
                        masked_clause += charac
                        flag = 1
                else:
                    masked_clause += morph.surface.strip('。、')
    return masked_clause

def noun2noun(lst, sentence):
    line_lst = []
    for i, l in enumerate(lst):
        clause_i = l[0]
        masked_clause_i = mask(clause_i, sentence, 'X')
        for x in range(len(lst)-i-1):
            clause_j = lst[i+x+1][0]
            masked_clause_j = mask(clause_j, sentence, 'Y')
            if clause_j in l: # 文節iから構文木の根に至る経路上に文節jが存在する場合
                idx = l.index(clause_j)
                line = ' -> '.join([masked_clause_i] + l[1:idx] + [masked_clause_j]) 
            elif (set(l) & set(lst[i+x+1])) != None: # 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合
                clause_k = list(set(l) & set(lst[i+x+1]))
                idx1 = l.index(clause_k[0])
                idx2 = lst[i+x+1].index(clause_k[0])
                line = ' -> '.join([masked_clause_i] + l[1:idx1]) + '|' + ' -> '.join([masked_clause_j] + lst[i+x+1][1:idx2]) + '|' + ' -> '.join(clause_k)
            else:
                pass
            line_lst.append(line)              
    return line_lst

if __name__ == '__main__':
    text = load_neko()
    lst = noun2root(text[7])
    for l in noun2noun(lst, text[7]):
        print(l)