def load_neko():
    with open('neko.txt.mecab') as f:
        lines = f.readlines()

    text = []
    sentence = []

    for line in lines:
        if line == 'EOS\n':
            text.append(sentence)
            sentence = []
        else:
            l = line.split('\t')
            ll = l[1].split(',')
            dic = {
                'surface': l[0],
                'base': ll[6],
                'pos': ll[0],
                'pos1': ll[1]
            }
            sentence.append(dic) 

    return text

if __name__ == '__main__':
    print(load_neko())