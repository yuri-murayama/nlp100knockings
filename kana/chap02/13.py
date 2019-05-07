#-*- coding: utf-8 -*-
#13.col1.txtとcol2.txtをマージ

# col1.txtとcol2.txtを読み込み、col1の改行は削除
with open('col1.txt', mode = 'r') as f:
	col1 = f.readlines()
col1 = [w.strip() for w in col1]

with open('col2.txt', mode = 'r') as f:
	col2 = f.readlines()

# col1とcol2を結合
col12 = [x + '\t' + y for x, y in zip(col1, col2)]

# col12ファイルに書き込み
with open('col12.txt', mode = 'w') as f:
	f.writelines(col12)

