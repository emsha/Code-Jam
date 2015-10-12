"""
Code jam practice: store credit: https://code.google.com/codejam/contest/351101/dashboard#s=p0

idea on how to solve. instead of searching throught hte list of prices to create the
perfect combo, let's look at the amount of money that we have and get all
of the possible combos from there and see if there are any pairs? would this be faster?

because your $$ will be less than 1000

yes i think this will work. every time you arrive at a number in the list of prodcut prices,
you add this number to a list (if the number and its coimpliment arent already in there.)
then we check if any of the lists in this list have len of 2
if so, we found our answer.
"""
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
# print "info = ", info
'''
    # info is a list of lists. each list is a test case.
    # info[n][x] returns certain info about the nth test case.
    x=0:how much money you have
    x=1:how many products in the store
    x=2:list of prices of the products

    ok this is how im gonna do this;
    clean list (remove duplicates if its odd and
    check if the middle number occurs twice
    if its even before doing so cuz if so, you have the answer)
    then say that : ok i have a sorted list so i'm just gonna go through
    and check the first and last elements. if they add up to money then nice else keep going
    then go back to the original list when you find your numbers and just go throug to find
    the solution indecies
'''
# solve
for casenum in range(len(info)):
    money = int(info[casenum][0])
    products = info[casenum][1].split()
    prices = info[casenum][2].split()
    ans = []
    # prices1 is a list of prices removing everything >= money
    # cuz you cant afford it and get two things
    prices1 = []
    for price in prices:
        if int(price) < money:
            prices1.append(int(price))
    # print prices1

    # lets solve:

    counter = [0 for x in range(money)]
    for price in prices1:
        counter[price] += 1
    if money % 2 == 0:
        if counter[money/2] > 0:
            ans = [money/2, money/2]
    if ans == []:
        for i in range(1, len(counter)/2):
            # print(i, ', ', len(counter) - i, counter[i], counter[len(counter) - i])
            if counter[i] > 0 and counter[len(counter) - i] > 0:
                ans = [i, len(counter) - i]
                break
    # format and return/print
    ans0index = prices.index(str(ans[0]))
    prices.reverse()
    ans1index = len(prices) - prices.index(str(ans[1])) - 1
    a = ("Case #", casenum + 1, ":", MIN(ans0index, ans1index) + 1, MAX(ans0index, ans1index) + 1)
    print '{0}{1}{2} {3} {4}'.format(*a)
    # print int(prices[ans0index]) + int(prices[ans1index]) == money
