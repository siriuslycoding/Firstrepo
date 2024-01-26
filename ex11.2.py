import re

file = open('mbox-short.txt')
total = 0
count = 0

for line in file :
    rline = line.rstrip()
    reqnum = re.findall('^New Revision: ([0-9]+)', rline)
    if reqnum :
        total += int(reqnum[0])
        count += 1

avg = total/count
print('Average is',avg)
file.close()
