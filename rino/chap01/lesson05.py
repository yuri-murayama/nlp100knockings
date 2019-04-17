# -*- coding: utf-8 -*-

def createWordNgram(s, n):
    """
    与えられたシーケンスから単語n-gramを作る関数

    args:
    - s: string  # 文章
    - n: int  # n-gramのn

    returns:
    - word_n_gram: string list # 単語n-gram
    """

    # 単語n_gramを作成
    word_n_gram = []
    word_list = s.split(" ")
    for i in range(0, len(word_list)-(n-1)):
        gram_list = [word_list[i+j] for j in range(n)]
        gram = " ".join(gram_list)
        word_n_gram.append(gram)

    return word_n_gram

def createCharNgram(s, n):
    """
    与えられたシーケンスから文字n-gramを作る関数

    args:
    - s: string  # 文章
    - n: int  # n-gramのn

    returns:
    - char_n_gram: string list # 文字n-gram
    """

    # 文字n_gramを作成
    char_n_gram = []
    char_list = "".join(s.split(" "))
    for i in range(0, len(char_list)-(n-1)):
        gram_list = [char_list[i+j] for j in range(n)]
        gram = "".join(gram_list)
        char_n_gram.append(gram)

    return char_n_gram

if __name__ == '__main__':
    s = "I am an NLPer"
    n = 2
    w_n_gram = createWordNgram(s, n)
    c_n_gram = createCharNgram(s, n)
    print("単語bigram: {}".format(w_n_gram))
    print("文字bigram: {}".format(c_n_gram))
