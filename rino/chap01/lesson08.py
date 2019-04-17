# -*- coding: utf-8 -*-

def cipher(strings):

    result = ""
    for s in strings:
        if s.islower():  # もし小文字なら
            result += chr(219-ord(s))
        else:
            result += s
    return result

if __name__ == '__main__':
    text = "I have a Pen."  # 変換後 I szev z Pvm.
    result = cipher(text)
    print(result)
