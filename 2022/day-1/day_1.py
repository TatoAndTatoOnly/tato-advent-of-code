fileobj=open("input-day-1.txt")
lines=fileobj.read()

from heapq import nlargest

cals = []
for chunk in lines.split("\n\n"):
    cals.append(sum(map(int, chunk.split())))

print("part a:", max(cals))
print("part b:", sum(nlargest(3, cals)))