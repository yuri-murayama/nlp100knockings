#-*- coding: utf-8 -*-
## 07.テンプレートによる文生成


def make_sentence(x,y,z):

	sentence = "x時のyはz"
	
	sentence = sentence.replace('x', str(x))
	sentence = sentence.replace('y', str(y))
	sentence = sentence.replace('z', str(z))

	return sentence


def main():
	print('x')
	x = input('>>')
	print('y')
	y = input('>>')
	print('z')
	z = input('>>')

	print(make_sentence(x,y,z))

if __name__ == '__main__':
	main()

