#-*- coding: utf-8 -*-
## 09.Typoglycemia
import random


def sort(word):

	if(len(word) < 5):
		return word
	else:
		sort_word = word[1:len(word)-1]
		sort_word = ''.join(random.sample(sort_word, len(sort_word)))
		
		sort_word = word[0] + sort_word + word[-1]

		return sort_word

def typoglycemia(text):

	text_word = text.split()
	sorted_text = ""

	for i, word in enumerate(text_word):
		sorted_text = sorted_text + sort(word) + " "

	return sorted_text	


def main():

	text = input()

	answer = typoglycemia(text)

	print (answer)

if __name__ == '__main__':
	main()

