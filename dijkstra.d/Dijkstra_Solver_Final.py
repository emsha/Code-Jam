# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:25:23 2015

@author: maxshashoua
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:47:36 2015

@author: maxshashoua
"""
"""Parsing"""
file = list(open('C-small-practice.in'))
for i in range(len(file)):
	file[i] = file[i].strip("\n").strip()
T = file.pop(0)

#parsing will spit out a list [number of iterations, code]

key = {'i':0, 'j':1, 'k':2, '1':3, '-1':4}
table = [['-1', 'k', '-j'], ['-k', '-1', 'i'], ['j', '-i', '-1']]


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


def checkNegOne(case):
    """check if the case will equal -1 when multiplied out from left to right"""
    # declare variables
    piece = case[2]
    pieceLen = int(case[0])
    numOfIters = int(case[1])
    totLen = pieceLen * numOfIters
    
    # now multiply out one piece to see if it is -1
    lastChar = '1'
    #print('first one')
    # iterate thorugh the piece.
    for i in range(pieceLen):
        modIndex = i % pieceLen
        newChar = piece[modIndex]
        lastChar = multiply(lastChar, newChar)
    
    # check based on number of iters and the value of the piece if it will be -1
    if lastChar == '1':
        return False
    elif lastChar == '-1':
        if numOfIters % 2 == 0:
            return False
    elif lastChar.__contains__('i'):
        if numOfIters % 2 != 0:
            return False
    elif lastChar.__contains__('j'):
        if numOfIters % 2 != 0:
            return False
    elif lastChar.__contains__('k'):
        if numOfIters % 2 != 0:
            return False
    return True


def solve(case):
    """checks whether you can make an ij"""
    # declare variables
    piece = case[2]
    pieceLen = int(case[0])
    numOfIters = int(case[1])
    totLen = pieceLen * numOfIters
    
    #find an i
    lastChar = '1'
    for i in range(totLen):
        modIndex = i % pieceLen
        newChar = piece[modIndex]
        lastChar = multiply(lastChar, newChar)
        if lastChar == 'i':
            # check for a j. (this works because we already checked if it all equals -1)
            lastCharj = '1'
            for j in range(i+1, totLen - 1):
                modIndex = j % pieceLen
                newCharj = piece[modIndex]
                lastCharj = multiply(lastCharj, newCharj)
                if lastCharj == 'j':
                    return True
    return False

t = 1
for i in [x for x in range(len(file)) if x % 2 == 0]:
    a = file[i].split(' ')    
    case = [a[0], a[1], file[i + 1]]
    #print(case)
    b = checkNegOne(case)    
    print('Case #' + str(t) + ': ' + str(b))
    t += 1

"""    if checkNegOne1(case) == False:
        print('2NO')
    if checkNegOne1(case) == True:
        print('2YES')
"""
 
'''    
    if checkNegOne(case) == False:
        print('NO')
    elif solve(case) == False:
        print('NO')
    else:
        print('YES')
'''
print('done')
