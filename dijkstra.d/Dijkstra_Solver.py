"""
So the algorithm is as follows:

search from the left for any combos from i = 0 to i = n - 2 that make an i. 
search from the right for any combos from i = -1 to i = (-(n-2)) that make a k.
now:
for every i, check with every k if the middle stuff is a j.

optimizations: 
First check whether the string has more than one letter.
Check whether the multiplication of the whole thing = -1.
When checking for i's, remember, if you find an i, the rest of the stuff MUST 
boil down to -j if there is even a chance of it being able to make j and k. 
Similarly, when checking for k's, the remaining stuff must boil down to i*j which is k.


instead of doing all i's then all k's, you could check for all i's, then for each k,
as you find it, check it with all the i's for a j before continuing the search for a new k.
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
            

def findIs(case):
    """takes in a list ['how long is str', 'how many?', 'str']"""
    print(case)
    iFound = []
    l = int(case[0])
    iters = int(case[1])
    s = case[2]
    n = l * iters
    lastChar = '1'
    for i in range(n-2):
        newChar = s[i%l]
        p = multiply(lastChar, newChar)
        #print(p)
        lastChar = p
        if p == 'i':
            iFound.append(i)
    print("iFound = ", iFound)
    return iFound
        
def findKs(case):
    """takes in a list ['how long is str', 'how many?', 'str']"""
    '''this is wrong as is. remember it has to go in order from the index of start to the end. now, it does something else and is wrong.'''
    #print(case)
    kFound = []
    l = int(case[0])
    iters = int(case[1])
    s = case[2]
    n = l * iters
    lastChar = '1'
    for i in list(range(2, n)).reverse():
        newChar = s[-(i%l)]
        
        #print("nC: ", newChar)
        p = multiply(newChar, lastChar)
        #print(p)
        lastChar = p
        if p == 'k':
            kFound.append(-i)
    print("kFound = ", kFound)
    return kFound
    
def findJs(case):
    listIIndex = findIs(case)
    listKIndex = findKs(case)
    for iIndex in listIIndex:
        for kIndex in listKIndex:
            jStart = iIndex + 1
            jEnd = kIndex
            if """they overlap""":
                break
            else:
                for c in r:
                    pass






def findJKs(case, iList):
    """takes in a list ['how long is str', 'how many?', 'str']"""
    '''this is wrong as is. remember it has to go in order from the index of start to the end. now, it does something else and is wrong.'''
    #print(case)
    kFound = []
    l = int(case[0])
    iters = int(case[1])
    s = case[2]
    n = l * iters
    lastChar = '1'
    for i in range(1, n):
        newChar = s[-(i%l)]
        #print("nC: ", newChar)
        p = multiply(newChar, lastChar)
        #print(p)
        lastChar = p
        if p == 'k':
            kFound.append(-i)
            for j in iList:
                lc = 1                
                for k in range(n - 1 - j):
                    nc = s[k%l]
                    jay = multiply(lc, nc)
                if jay == "J":
                    return True
                
                
    print("kFound = ", kFound)
    

    
    
for i in [x for x in range(len(file)) if x % 2 == 0]:
    a = file[i].split(' ')    
    c = [a[0], a[1], file[i + 1]]
    findIs(c)
    findKs(c)
    #findJs(c)