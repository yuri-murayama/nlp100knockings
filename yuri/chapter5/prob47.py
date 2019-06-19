from prob41 import load_neko
from prob43 import contain_pos
from prob45 import get_left_morph, get_right_morph

def contain_sahen_noun_wo(chunk, pos_name, pos1_name, p_name):
    booll = False
    for i, morph in enumerate(chunk.morphs):
        if i < len(chunk.morphs)-1:
            if morph.pos == pos_name and morph.pos1 == pos1_name and chunk.morphs[i+1].surface == p_name:
                booll = True
    return booll

def get_sahen_noun_wo_verb(sentence):
    lst = []
    for chunk in sentence:
        if contain_sahen_noun_wo(chunk, '名詞', 'サ変接続', 'を') and contain_pos(sentence[chunk.dst], '動詞'):
            plst = []
            clst = []
            for i in sentence[chunk.dst].srcs:
                if contain_pos(sentence[i], '助詞') and not contain_sahen_noun_wo(sentence[i], '名詞', 'サ変接続', 'を'):
                    plst.append(get_right_morph(sentence[i], '助詞'))
                    clst.append(''.join([morph.surface.strip('。、') for morph in sentence[i].morphs]))
            if len(plst) > 0:
                predicate = get_left_morph(chunk, '名詞') + 'を' + get_left_morph(sentence[chunk.dst], '動詞')
                lst.append((predicate, ' '.join(plst), ' '.join(clst)))
    return lst

if __name__ == '__main__':
    text = load_neko()
    with open('sahen_noun_wo_verb.txt', 'w', encoding='utf-8') as f:
        for sentence in text:
            for t in get_sahen_noun_wo_verb(sentence):
                f.write(t[0] + '\t' + t[1] + '\t' + t[2] + '\n')

'''
コーパス中で頻出する述語（サ変接続名詞+を+動詞）
sort sahen_noun_wo_verb.txt | uniq -c | sort -r | cut -f 1
2 休養を要する
1 ストライキをしでかす
1 御馳走を食わせる
1 ストライキを起す
1 いたずらを始める

コーパス中で頻出する述語と助詞パターン
sort sahen_noun_wo_verb.txt | uniq -c | sort -r
2 休養を要する       は      　吾輩はまた
1 ストライキをしでかす       から て 云うから なって
1 御馳走を食わせる   から て に      してやるから 大事にして 晩に
1 ストライキを起す   て が に        なって 活気が 一度に
1 いたずらを始める   は て   独仙君とは 引きずり出して
'''