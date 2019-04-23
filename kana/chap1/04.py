#-*- coding: utf-8 -*-

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

number = [1,5,6,7,8,9,15,16,19]

text = text.replace(',' ,'')
text = text.replace('.', '')

text = text.split()

dictionary = {}

for i in range(len(text)):
	if(i+1 in number):
		dictionary[i+1] = text[i][0]
	else:
		dictionary[i+1] = text[i][0:2]

print(dictionary)
