import re
import regex
import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

def get_phrase(parsed_sentence):
    global phrase_lst
    p1 = re.compile(r'^\((.*?)\s(.*)\)$')   
    m = p1.match(parsed_sentence)
    tag = m.group(1)
    rest = m.group(2)
    p2 = r'(?<rec>\((?:[^()]+|(?&rec))*\))' # 再帰を使って、入れ子のカッコの一番外側を取る
    parseds = regex.findall(p2, rest)
        
    if parseds == []:
        phrase_lst.append((tag, rest))
        return rest
    else:
        word_lst = []
        for p in parseds:
            word_lst.append(get_phrase(p))
        phrase = ' '.join(word_lst)
        phrase_lst.append((tag, phrase))
        return phrase

with open('output59.txt', 'w') as f:    
    for parse in tree.iter('parse'):
        phrase_lst = []
        get_phrase(parse.text.strip())
        for t in phrase_lst:
            if t[0] == 'NP':
                f.write(t[1] + '\n')