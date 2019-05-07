#-*- coding: utf-8 -*-
## 05.n-gram

def make_n_gram(text,n):
	
	n_gram = []

	for i in range(0, len(text)-1):
		n_gram.append(text[i] + text[i+1])

	return n_gram	

def main():
	text = input()
	
	#単語bi-gram
	text_word = text.split()
	print(make_n_gram(text_word, 2))

	#文字bi-gram
	text = text.replace(' ', '')
	print(make_n_gram(text, 2))

if __name__ == '__main__':
	main()

