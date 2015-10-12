# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:47:36 2015

@author: maxshashoua
"""
"""Parsing"""
file = list(open('Dijkstra_tinyInput_mod.txt'))
for i in range(len(file)):
	file[i] = file[i].strip("\n").strip()
T = file.pop(0)
#print(file)

#parsing will spit out a list [number of iterations, code]

key = {'i':0, 'j':1, 'k':2, '1':3, '-1':4}
table = [['-1', 'k', '-j'], ['-k', '-1', 'i'], ['j', '-i', '-1']]
negOneTable = ['-i', '-j']


def multiply(a, b):
    """a*b, takes in strings, returns strings"""
    if a == "1":
        return b
    elif b == "1":
        return a
    elif a == '-1':
        if len(b) == 2:
            return b.strip('-')
        else:
            return b
    elif b == '-1':
        if len(a) == 2:
            return a.strip('-')
        else:
            return a
    else:
        neg = 0
        if len(a) == 2:
            neg += 1
        if len(b) == 2:
            neg += 1
        a = key.get(a.strip('-'))
        b = key.get(b.strip('-'))
        p = table[a][b]        
        if len(p) == 2:
            neg += 1
            p = p[1]
        if neg % 2 == 0:
            return p
        else:
            return "-" + p
