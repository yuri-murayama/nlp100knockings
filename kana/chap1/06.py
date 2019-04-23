#-*- coding: utf-8 -*-
## 05.n-gram


def make_n_gram_char(text,n):
	
	n_gram = []

	for i in range(0, len(text)-1):
		n_gram.append(text[i] + text[i+1])

	return n_gram	

def main():
	text1 = "paraparaparadise"
	text2 = "paragraph"
	
	X = make_n_gram_char(text1, 2)
	Y = make_n_gram_char(text2, 2)

	# 和集合
	print("和集合")
	print(set(X+Y))
	# 差集合
	print("差集合")
	print(set(X)-set(Y))
	# 積集合
	print("積集合")
	print(set(X) & set(Y))
	#'se'が含まれるかどうか
	print("'se'が含まれるかどうか")
	print('X: {} '.format('se' in X))
	print('Y: {} '.format('se' in Y))

if __name__ == '__main__':
	main()

