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

# solve
for casenum in range(len(info)):
    money = int(info[casenum][0])
    products = info[casenum][1].split()
    prices = info[casenum][2].split()
    intprices = []
    ans = []
    for i in prices:
        if int(i) < money:
            intprices.append(int(i))
    # print prices

    # create and fill counter list
    counter = [0 for x in range(1, money + 1)]
    print money
    for p in intprices:
        # print "/",p
        counter[p] += 1

    # find the answer :)
    for i in range(len(counter)//2):
        if counter[i] > 0 and counter[len(counter) - i] > 0:
            ans = [intprices.index(i)]
            intprices.reverse()
            ans.append(intprices.index(len(counter) - i))
            break
        elif i == len(counter) - i and counter[i] > 1:
            ans = [intprices.index(i)]
            intprices.reverse()
            ans.append(intprices.index(i))
    print ans
