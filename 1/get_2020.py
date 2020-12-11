file1 = open('entry.txt', 'r')
Lines = file1.readlines()

for n in range(len(Lines)):
    base = int(Lines[n])
    for i in range(n,len(Lines)):
        other = int(Lines[i])
        for j in range(i,len(Lines)):
            another_other = int(Lines[j])
            if base + other + another_other == 2020:
                print(f"{base} * {other} * {another_other} = {base * other * another_other} ")

