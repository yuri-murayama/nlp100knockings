#-*- coding: utf-8 -*-

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

text = text.replace(',', '')
text = text.replace('.', '')

text = text.split()

for word in text:
	print(len(word), end = "")
print()	