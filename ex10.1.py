file = open('mbox-short.txt')
emailids = list()
idfreq = dict()

for line in file:
    if line.startswith('From '):
        words = line.split()
        emailids.append(words[1])

for email in emailids:
    idfreq[email] = idfreq.get(email, 0) + 1

#print(idfreq)

freqlist = list()
for email,freq in idfreq.items() :
    new = (freq,email)
    freqlist.append(new)

freqlist.sort(reverse = True)
print("Person with the most commits is:")
print(freqlist[0])
