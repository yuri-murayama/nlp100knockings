import re
import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

# {文番号: 参照表現リスト}の辞書作成
mention_dict = {}
for mention in tree.iter('mention'):
    if mention.attrib:
        representative = mention.find('text').text
    else:
        sen_num = int(mention.find('sentence').text) # 何文目か
        mention_lst = [            
            int(mention.find('start').text),
            int(mention.find('end').text),
            representative,
            mention.find('text').text
            ]
        if sen_num not in mention_dict:
            mention_dict[sen_num] = [mention_lst]
        else:
            mention_dict[sen_num].append(mention_lst)  

# 前から置換していったときのインデックスのずれを考えるのが面倒臭いので、後ろ順に並び替え
mention_dict = {k: sorted(sorted(v, key=lambda x: x[0]), key=lambda x: -x[1]) for k, v in mention_dict.items()}


sentences = []
for sentence in tree.iter('sentence'):
    words = []
    for word in sentence.iter('word'):
        words.append(word.text)
    if len(words) > 0:
        sentences.append(words)
        
black_lst = [12, 24, 40, 46]

with open('output56.txt', 'w') as f:
    for i, sentence in enumerate(sentences, 1):
        if i in mention_dict:
            start = 0
            end = 0
            for l in mention_dict[i]:
                start0 = l[0]
                end0 = l[1]
                if start0 >= start and end0 <= end: # 入れ子
                    result = re.search(r'（.+）', sentence[start-1])
                    s = result.group().strip('（）').split()
                    rs = result.start()
                    s = s[:start0-start] + ['「{0}（{1}）」'.format(l[2], l[3])] + s[end0-start:]
                    sentence[start-1] = sentence[start-1][:rs+1] + ' '.join(s) + '）」'
                else:
                    start = l[0]
                    end = l[1]
                    sentence = sentence[:start-1] + ['「{0}（{1}）」'.format(l[2], l[3])] + sentence[end-1:] 
        f.write(' '.join(sentence) + '\n')            
        if i in black_lst:
            print(mention_dict[i])
            print(' '.join(sentences[i-1]))
            print(' '.join(sentence))           
            print('')

'''
[[36, 38, 'My head', 'your head'], [36, 37, 'you', 'your'], [26, 27, "the `` patient ''", 'My'], [13, 14, 'ELIZA', 'ELIZA']]
When the `` patient '' exceeded the very small knowledge base , ELIZA might provide a generic response , for example , responding to `` My head hurts '' with `` Why do you say your head hurts ? ''
When the `` patient '' exceeded the very small knowledge base , 「ELIZA（ELIZA）」 might provide a generic response , for example , responding to `` 「the `` patient ''（My）」 head hurts '' with `` Why do you say 「My head（「you（your）」 head）」 hurts ? ''

[[12, 31, 'a solved problem', 'machine translation , due especially to work at IBM Research , where successively more complicated statistical models were developed'], [12, 14, 'a solved problem', 'machine translation']]
Many of the notable early successes occurred in the field of machine translation , due especially to work at IBM Research , where successively more complicated statistical models were developed .
Many of the notable early successes occurred in the field of 「a solved problem（「a solved problem（machine translation）」 , due especially to work at IBM Research , where successively more complicated statistical models were developed）」 .

[[9, 27, 'statistical models', 'statistical models , which make soft , probabilistic decisions based on attaching real-valued weights to each input feature'], [21, 23, 'real-valued weights', 'real-valued weights'], [14, 18, 'soft , probabilistic decisions', 'soft , probabilistic decisions'], [9, 11, 'statistical models', 'statistical models']]
Increasingly , however , research has focused on statistical models , which make soft , probabilistic decisions based on attaching real-valued weights to each input feature .
Increasingly , however , research has focused on 「statistical models（「statistical models（statistical models）」 , which make 「soft , probabilistic decisions（soft , probabilistic decisions）」 based on attaching 「real-valued weights（real-valued weights）」 to each input feature）」 .

[[19, 29, 'the rules', 'the rules , which is a much more difficult task'], [19, 21, 'the rules', 'the rules'], [3, 8, 'the systems', 'systems based on hand-written rules'], [6, 8, 'hand-written rules', 'hand-written rules']]
However , systems based on hand-written rules can only be made more accurate by increasing the complexity of the rules , which is a much more difficult task .
However , 「the systems（systems based on 「hand-written rules（hand-written rules）」）」 can only be made more accurate by increasing the complexity of 「the rules（「the rules（the rules）」 , which is a much more difficult task）」 .
'''