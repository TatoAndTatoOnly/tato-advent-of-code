def IntersecOfSets(arr1, arr2, arr3):
    # Converting the arrays into sets
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
      
    # Calculates intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)         #[80, 20, 100]
      
    # Calculates intersection of sets
    # on set1 and s3
    result_set = set1.intersection(s3)
    
    # Converts resulting set to list
    final_list = list(result_set)
    return(final_list[0])

fileobj=open("input-day-3.txt")
priority = 0
elf1 = []
elf2 = []
elf3 = []
priorities = []
dif = []
group = []
j = 0

import string

az_Lower = string.ascii_lowercase
az_Upper = string.ascii_uppercase
az_Lower = az_Lower + az_Upper
for i in az_Lower:
    priorities.append(i)

print(priorities)

lines=fileobj.read().split('\n')

for sack in lines:
    group.append(sack)
    j = int(j) + 1
    if j == 3:
        for item in group[0]:
            elf1.append(item)
        for item in group[1]:
            elf2.append(item)
        for item in group[2]:
            elf3.append(item)
        badge = IntersecOfSets(elf1, elf2, elf3)
        priority += priorities.index(badge)
        priority += 1
        elf1 = []
        elf2 = []
        elf3 = []
        group = []
        j = 0

print(priority)

        
