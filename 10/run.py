file1 = open('input.txt', 'r')
Lines = file1.readlines()
adapters = []
for line in Lines:
    line = line.strip("\n")
    adapters.append(int(line))
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()
dif1 = 0
dif3 = 0
#Part1
for i in range(1,len(adapters)):
    if adapters[i]-adapters[i-1]==1:
        dif1 +=1
    if adapters[i]-adapters[i-1]==3:
        dif3 +=1

print(f"Result Part 1: {dif1} * {dif3} = {dif1 * dif3}")

#Part 2. Thanks to kaur_virunurm
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfbo61q/?utm_source=reddit&utm_medium=web2x&context=3
from collections import Counter
c = Counter({0:1})
for x in adapters:
    c[x+1] += c[x]
    c[x+2] += c[x]
    c[x+3] += c[x]

print("Part 2:", c[max(adapters) + 3])
