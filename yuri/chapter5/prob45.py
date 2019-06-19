from prob41 import load_neko
from prob43 import contain_pos

def get_left_morph(chunk, pos_name):
    for morph in chunk.morphs:
        if morph.pos == pos_name:
            return morph.base

def get_right_morph(chunk, pos_name):
    for morph in chunk.morphs:
        if morph.pos == pos_name:
            r = morph.base
    return r

def get_case_pattern(sentence):
    lst = []
    for chunk in sentence:
        if contain_pos(chunk, '動詞'):
            plst = []
            for i in chunk.srcs:
                if contain_pos(sentence[i], '助詞'):
                    plst.append(get_right_morph(sentence[i], '助詞'))
            if len(plst) > 0:
                lst.append((get_left_morph(chunk, '動詞'), ' '.join(plst)))
    return lst

if __name__ == '__main__':
    text = load_neko()
    with open('case_pattern.txt', 'w', encoding='utf-8') as f:
        for sentence in text:
            for t in get_case_pattern(sentence):
                f.write(t[0] + '\t' + t[1] + '\n')

'''
コーパス中で頻出する述語と格パターンの組み合わせ
sort case_pattern.txt | uniq -c | sort -r

706 云う       と
448 する       を
331 思う       と
202 ある       が
199 なる       に
190 する       に
178 見る       て
161 する       と
117 する       が
 98 見る       を


「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
sort case_pattern.txt | grep 'する' | uniq -c | sort -r
448 する       を
190 する       に
161 する       と

sort case_pattern.txt | grep '見る' | uniq -c | sort -r
178 見る       て
 98 見る       を
 24 見る       て て

sort case_pattern.txt | grep '与える' | uniq -c | sort -r
4 与える     に を
2 与える     て に を
1 与える     けれども は を
'''