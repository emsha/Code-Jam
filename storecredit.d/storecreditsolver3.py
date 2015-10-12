# max and MIN
def MAX(a, b):
    if a >= b:
        return a
    return b

def MIN(a, b):
    if a <= b:
        return a
    return b

"""Parsing"""
file = list(open('A-large-practice.in'))
for i in range(len(file)):
    file[i] = file[i].strip("\n").strip()
N = file.pop(0)
    # N is the number of test cases in this file
    # file is now a list of lines in the file

info = []
for i in range(len(file)/3):
    temp = [file[i*3], file[i*3 + 1], file[i*3 + 2]]
    info.append(temp)
# info[i][j] ... switch j{0 : money, 1 : #products, 2 : prices list}

# solve
for casenum in range(len(info)):
    # print casenum
    money = int(info[casenum][0])
    products = info[casenum][1].split()
    prices = info[casenum][2].split()
    intprices = []
    for i in prices:
        intprices.append(int(i))

    # make counter
    counter = [0 for x in range(money + 1)]

    # fill up counter
    for i in intprices:
        if i < money:
            counter[i] += 1

    # solve
    index1 = 0
    index2 = 0
    for i in range(1, money + 1):
        if counter[i] > 0 and counter[money - i] > 0:
            # print money, i, money - i
            index1 = prices.index(str(i))
            index2 = prices.index(str(money - i))
            break

    if index1 == index2:
        pricesshort = prices[index2 + 1:]
        index2 += pricesshort.index(str(i)) + 1
    # print index1, index2
    a = ['Case #', casenum + 1, ':', MIN(index1, index2) + 1, MAX(index1, index2) + 1]
    print '{0}{1}{2} {3} {4}'.format(*a)
    # print int(prices[index1]) + int(prices[index2]) == money
