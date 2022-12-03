fileobj=open("input.txt")
points = 0

lines=fileobj.read().split('\n')

for moves in lines:
    if moves == "A X":
        points += 4
    elif moves == "A Y":
        points += 8
    elif moves == "A Z":
        points += 3
    elif moves == "B X":
        points += 1
    elif moves == "B Y":
        points += 5
    elif moves == "B Z":
        points += 9
    elif moves == "C X":
        points += 7
    elif moves == "C Y":
        points += 2
    elif moves == "C Z":
        points += 6
    else:
        pass

print("the answer is", points)



