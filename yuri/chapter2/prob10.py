import sys
from operator import itemgetter

with open("hightemp.txt", encoding='utf-8') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

# 10
len_lines = len(lines)
print('問題10\n', len_lines)

# wc -l hightemp.txt

# 11
new_lines = [l.replace('\t', ' ') for l in lines]
print('問題11\n', new_lines)

# sed -e 's/\t/ /g' hightemp.txt

# 12
col1 = []
col2 = []
for l in new_lines:
    l = l.split(' ')
    col1.append(l[0])
    col2.append(l[1])

with open("col1.txt", 'w') as f:
    f.write('\n'.join(col1))
with open("col2.txt", 'w') as f:
    f.write('\n'.join(col2))

# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt

# 13
with open("col1.txt", encoding='utf-8') as f:
    col1_lines = f.readlines()
with open("col2.txt", encoding='utf-8') as f:
    col2_lines = f.readlines()
    
with open("merged.txt", 'w') as f:
    for c1, c2 in zip(col1_lines, col2_lines):
        c1 = c1.strip()
        c2 = c2.strip()
        f.write(c1 + '\t' + c2 + '\n')

# paste col1.txt col2.txt

# 14
N = int(sys.argv[1])
print('問題14\n', new_lines[:N])

# head -n 3 hightemp.txt

# 15
print('問題15\n', new_lines[:-N-1:-1])

# tail -n 3 hightemp.txt

# 16
print('問題16')
if N > len_lines:
    print('impartible')
else:
    x = int(len_lines / N)
    for i in range(N):
        print(new_lines[i*x:(i+1)*x])

# split -l 8 hightemp.txt

# 17
col1_lines = [l.strip() for l in col1_lines]
print('問題17\n', set(col1_lines))

# sort col1.txt | uniq

# 18
multi_lines = [l.split(' ') for l in new_lines] # 多次元化
multi_lines.sort(key=itemgetter(2))
multi_lines.reverse()
print('問題18\n', multi_lines)

# sort -r -k 3 hightemp.txt

# 19
dic = {}
for l in col1_lines:
    if l not in dic:
        dic[l] = 1
    else:
        dic[l] += 1

dic = sorted(dic.items(), key=lambda x: -x[1])
print('問題19\n', dic)

# sort col1.txt | uniq -c | sort -r -k 1