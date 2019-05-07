#-*- coding: utf-8 -*-
## 08.暗号文


def cipher(text):

	for i in range(len(text)):
		if(text[i].islower()):
			text = text.replace(text[i],str(ord(text[i])))

	return(text)		

def main():

	text = input()

	print(cipher(text))

if __name__ == '__main__':
	main()

