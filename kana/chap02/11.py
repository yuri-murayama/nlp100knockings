#-*- coding: utf-8 -*-
#11.タブをスペースに置換

# ファイルを読み込んで、tabをスペースに置き換え
with open('hightemp.txt', mode = 'r') as f:
	text = f.read()
	text_remove_tab = text.replace('\t', ' ')

# ファイルに出来上がったテキストを書き込み
with open('hightemp_11.txt', mode = 'w') as f:
	f.write(text_remove_tab)
