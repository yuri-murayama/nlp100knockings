import collections

cal1 = []
with open("hightemp2.txt", "r") as f:
    for line in f:
        l = line.split(' ')
        cal1.append(l[0])
    ans = collections.Counter(cal1) #Counter(リスト)：リストの中の要素の出現回数を取得し辞書のように保持
    for k,v in sorted(ans.items(), key = lambda x : -x[1]):
        print(k+':'+str(v))

# cat hightemp.txt | cut -f 1 | sort | uniq -c | sort -r
#１行目を取り出して昇順に並べて、重複している行数を先頭に付加して、重複を取り除く.逆順に並び替える
