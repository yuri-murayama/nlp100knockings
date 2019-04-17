# -*- coding: utf-8 -*-

def returnText(x,y,z):
    text = "{}時の{}は{}".format(x,y,z)
    return text

if __name__ == '__main__':
    x=12
    y="気温"
    z=22.4
    text = returnText(x,y,z)
    print(text)
