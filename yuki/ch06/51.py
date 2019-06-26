#空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力

with open('output50.txt','r') as f:
    with open('output51.txt','w') as outputf:
        lines = f.readlines()
        for line in lines:
            line = line.strip(',')
            line = line.strip('.')
            line = line.strip(':')
            words = line.split()
            for word in words:
                outputf.write(word+'\n')
