from prob30 import load_neko

def count(text):
    dic = {}
    for sentence in text:
        for morpheme in sentence:
            if morpheme['base'] not in dic:
                dic[morpheme['base']] = 1
            else:
                dic[morpheme['base']] += 1            

    dic = sorted(dic.items(), key=lambda x: -x[1])
    return dic

if __name__ == '__main__':
    text = load_neko()
    dic = count(text)
    print(dic)