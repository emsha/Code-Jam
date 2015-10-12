# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:00:02 2015

@author: maxshashoua
"""
'''
file = open('B-small-practice.in')
T = file[0]
print(T)
'''

def change(p, c):
    ch = p - c
    l = []
    if ch <= 0:
        print('no change needed or not enough money!!')
    else:
        print(ch)
        print(makeChange(ch, l))
        print(l)

def makeChange(ch, l):
    if ch == 0:
        return 0
    elif ch - 100 >= 0:
        l.append(100.00)
        makeChange(ch - 100.00, l)
    elif ch - 50 >= 0:
        l.append(50.00)
        makeChange(ch - 50.00, l)
    elif ch - 20 >= 0:
        l.append(20.00)
        makeChange(ch - 20.00, l)
    elif ch - 10 >= 0:
        l.append(10.00)
        makeChange(ch - 10.00, l)
    elif ch - 5 >= 0:
        l.append(5.00)
        makeChange(ch - 5.00, l)
    elif ch - 1 >= 0:
        l.append(1.00)
        makeChange(ch - 1.00, l)
    elif ch - 0.25 >= 0:
        l.append(0.25)
        makeChange(ch - 0.25, l)
    elif ch - 0.10 >= 0:
        l.append(0.10)
        makeChange(ch - 0.10, l)
    elif ch - 0.05 >= 0:
        l.append(0.05)
        makeChange(ch - 0.05, l)
    elif ch - 0.01 >=  0:
        l.append(0.01)
        makeChange(ch - 0.01, l)

change(100, 53.71)