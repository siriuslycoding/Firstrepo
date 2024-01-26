file = open('mbox-short.txt')
hourl = list()

for line in file:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hourpos = time.find(':')
        hour = time[:hourpos]
        hourl.append(hour)

hourfreq = dict()
for hour in hourl:
    hourfreq[hour] = hourfreq.get(hour, 0) + 1

sorted(hourfreq.keys())
for hour,freq in hourfreq.items():
    print(hour,freq)
