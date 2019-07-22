import re

def ch_sent():
    with open('nlp.txt','r', encoding='utf-8') as f:
        for line in f:
            ln = re.sub(r'(\.|;|:|\?|!)(\s+)([A-Z])', r'\n', line)
            sent = re.split(r'\n',ln)
            for i in filter(lambda x: len(x) > 0, sent):
                print(i)
                yield i

def main():
    with open('py50.txt', 'w', encoding='utf8') as f2:
        for ln2 in ch_sent():
            f2.write(ln2 + '\n')

if __name__ == '__main__':
    main()
