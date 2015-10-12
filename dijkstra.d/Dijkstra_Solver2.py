# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:48:54 2015

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

def solve(case):
    l = int(case[0])
    iters = int(case[1])
    s = case[2]
    n = l * iters
    lastChar = '1'
    for i in range(n):
        newChar = s[i%l]
        p = multiply(lastChar, newChar)
        #print(p)
        lastChar = p
    if lastChar != '-1':
        return False
    for i in range(n-2):
        newChar = s[i%l]
        p = multiply(lastChar, newChar)
        #print(p)
        lastChar = p
        if p == 'i':
            for j in range(i+1, n-1):
                print(j)


for i in [x for x in range(len(file)) if x % 2 == 0]:
    a = file[i].split(' ')    
    c = [a[0], a[1], file[i + 1]]
    solve(c)