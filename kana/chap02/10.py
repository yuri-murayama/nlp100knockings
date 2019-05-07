#-*- coding: utf-8 -*-
#10.行数のカウント

with open('hightemp.txt', mode = 'r') as f:
	text = f.readlines()
print(len(text))