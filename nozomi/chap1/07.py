# -*- coding: utf-8 -*-     

ex = (12,'気温',22.4)
def moziretsu(x,y,z):
    s=('{}の時の{}は{}'.format(x,y,z))

    return s

x = 12
y = '気温'
z = 22.4
s = moziretsu(x,y,z)
print(s)
