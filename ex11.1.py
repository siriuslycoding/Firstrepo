import re

file = open('mbox-short.txt', 'r')
strlist = list()
reqstr = input('Enter a regular expression: ')

for line in file :
    realline = line.rstrip()
    matches = re.findall(reqstr, realline)
    strlist.extend(matches)
num = len(strlist)

print('mbox-short.txt had',num,'lines that matched',reqstr)
