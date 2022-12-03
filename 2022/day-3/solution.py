fileobj=open("input-day-3.txt")
priority = 0
comp1list = []
comp2list = []
priorities = []
dif = []

import string

az_Lower = string.ascii_lowercase
az_Upper = string.ascii_uppercase
az_Lower = az_Lower + az_Upper
for i in az_Lower:
    priorities.append(i)

print(priorities)

lines=fileobj.read().split('\n')

for sack in lines:
    size = len(sack)
    sep = size // 2
    comp1 = sack[:sep]
    comp2 = sack[sep:]
    for item in comp1:
        comp1list.append(item)
    for item in comp2:
        comp2list.append(item)
    same = str(set(comp1list).intersection(comp2list))
    same = same[2]
    dif.append(same)
    priority += priorities.index(same)
    priority += 1
    print(priority)
    comp1list = []
    comp2list = []

print(dif)


