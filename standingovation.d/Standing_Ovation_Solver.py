# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:13:16 2015

@author: maxshashoua
"""

file = list(open("Standing_Ovation_Large.in"))

for i in range(len(file)):
    file[i] = file[i].strip("\n").strip()

T = int(file[0])
Total = T

data = file[1:]

""""
for l in data:
    t = l[0]
    s = 1
    friends = 0
    raw = l[2:]
    # j in raw is each character in the raw data for number of people in one puzzle
    for j in raw:
        s -= 1
        s += int(j)        
        if s == 0:
            friends += 1
            s += 1
 
    print('Case #' + str(Total - T + 1) + " " + str(friends))
    T -= 1
"""
f = open("Standing_Ovation_Large_Attempt.txt", "w")

for l in data:
    t = l[0]
    s = 1
    friends = 0
    rawP = l.split(" ")
    raw = rawP[1]
    # j in raw is each character in the raw data for number of people in one puzzle
    for j in raw:
        s -= 1
        s += int(j)        
        if s == 0:
            friends += 1
            s += 1
    f.write('Case #' + str(Total - T + 1) + " " + str(friends) + "\n")
    print('Case #' + str(Total - T + 1) + " " + str(friends) + "\n")
    T -= 1
    
print("done")