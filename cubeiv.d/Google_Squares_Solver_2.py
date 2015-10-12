# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:45:01 2015

@author: maxshashoua
"""

file = list(open("A-large-practice.in"))

#file = list(open("tinyPractice.in"))

for l in range(len(file)):
    file[l] = file[l].strip("\n").strip()

T = file[0]
startIndices = []
#lines = list(range(2, len(file))):
x = 2
while x < len(file):
    startIndices.append(x)
    x += int(file[x]) + 1
    

#print(file)


#s = side, i = index of defining line of puzzle
# to access grid, it is grid[y, x]
class Puzzle(object):
    def __init__(self, i):
        self.size = int(file[i])
        self.rows = [file[y] for y in range(i + 1, i + 1 + self.size)]
        self.grid = []
        self.visited = set()
        for r in self.rows:
            l = r.split(' ')
            for i in range(len(l)):
                l[i] = int(l[i])
            self.grid.append(l)
                     
    def solve(self):
        d = [0, 0]
        # d = {how far:starting number}
        for y in range(self.size):
            for x in range(self.size):
                m = self.look(x, y)
                #print(m, ":", self.grid[y][x])
                if m > d[0]:
                    d = [m, self.grid[y][x]]
                elif m == d[0]:
                    if self.grid[y][x] < d[1]:
                        d[1] = self.grid[y][x]
        return d

    def look(self, x, y):
        home = self.grid[y][x]
        if self.visited.__contains__(home):
            return 0
        else:
            self.visited.add(home)        
            try:
                if self.grid[y + 1][x] - home == 1:
                    return self.look(x, y + 1) + 1
            except RuntimeError:
                pass
            try:
                if self.grid[y - 1][x] - home == 1:
                    return self.look(x, y - 1) + 1
            except IndexError:
                pass
            try:
                if self.grid[y][x + 1] - home == 1:
                    return self.look(x + 1, y) + 1
            except IndexError:
                pass
            try:
                if self.grid[y][x - 1] - home == 1:
                    return self.look(x - 1, y) + 1
            except IndexError:
                pass
            return 1
            
    
#p = Puzzle(8)
#print(p.rows)
#print(p.solve())



for i in range(len(startIndices)):
    p = Puzzle(startIndices[i])
    size = file[startIndices[i]]
    s = p.solve()
    print("Case #" + str(i + 1) + ":", s[1], s[0])