def get_set(input_string):
    list_elements = []
    for i in range(len(input_string)):
        list_elements.append(input_string[i])
    return set(list_elements)

file1 = open('input.txt', 'r')
Lines = file1.readlines()

groups = []
group = []
first = True
for line in Lines:
    line = line.strip("\n")
    if line=="":
        groups.append(group)
        print("Nuevo grupo")
        group = []
        first = True
    else:
        if first:
            group = get_set(line)
        else:
            new_group = get_set(line)
            tmp_group = group & new_group
            group = tmp_group
        first = False

groups.append(group)
print(f"Groups = {groups}")

suma = 0
for i in range(len(groups)):
    suma += len(groups[i])

print(f"Suma = {suma}")

