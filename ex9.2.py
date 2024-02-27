file = open('mbox-short.txt')
days_in_file = list()
daycount = dict()
for line in file:
    if line.startswith('From '):
        words = line.split()
        days_in_file.append(words[2])
for day in days_in_file:
    daycount[day] = daycount.get(day, 0) + 1
print(daycount)
