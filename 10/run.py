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
dif2 = 0
dif3 = 0

#Part1
for i in range(1,len(adapters)):
    if adapters[i]-adapters[i-1]==1:
        dif1 +=1
    if adapters[i]-adapters[i-1]==2:
        dif2 +=1
    if adapters[i]-adapters[i-1]==3:
        dif3 +=1

print(f"Result Part 1: {dif1} * {dif3} = {dif1 * dif3}")
