#-*- coding: utf-8 -*-

text1 = "パトカー"
text2 = "タクシー"

text = text1 + text2

for i in range(len(text1)):
	print(text[i:8:4], end = "")
	
print ()