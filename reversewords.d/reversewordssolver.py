def solve(s):
    s = s.split()
    s.reverse()
    return s

file = list(open("B-large-practice.in"))
for i in range(len(file)):
    file[i] = file[i].strip("\n").strip()
N = file.pop(0)

print file

# file is now a list of all the cases. each case is a string of the words separaed by spaces
# create file to write to
f = open("B-large-practice-out.txt", "w")

for case in range(len(file)):
    solvedlist = solve(file[case])
    solvedstring = ' '.join(solvedlist)
    f.write('Case #')
    f.write(str(case + 1))
    f.write(': ')
    f.write(solvedstring)
    f.write('\n')
print 'done'
