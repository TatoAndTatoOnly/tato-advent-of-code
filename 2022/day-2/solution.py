fileobj=open("input.txt")
points = 0
for line in fileobj:
    if line == "A X":
        points += 4
    elif line == "A Y":
        points += 8
    elif line == "A Z":
        points += 3
    elif line == "B X":
        points += 1
    elif line == "B Y":
        points += 5
    elif line == "B Z":
        points += 9
    elif line == "C X":
        points += 7
    elif line == "C Y":
        points += 2
    elif line == "C Z":
        points += 6
    else:
        pass
print("the answer is", points)


