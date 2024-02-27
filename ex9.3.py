file = open('mbox-short.txt')
emailids = list()
idfreq = dict()
for line in file:
    if line.startswith('From '):
        words = line.split()
        emailids.append(words[1])
for email in emailids:
    idfreq[email] = idfreq.get(email, 0) + 1
print(idfreq)
maxid = None
maxnum = None
for id,num in idfreq.items():
    if maxnum is None or num > maxnum:
        maxnum = num
        maxid = id
print(maxid,'(',maxnum,') has sent the most messages.')
