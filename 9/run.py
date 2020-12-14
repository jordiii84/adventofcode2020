def find_sum(array, item):
    for i in range(len(array)-1):
        if item-array[i] in array and item-array[i]!=array[i]:
            return True
    return False


file1 = open('input.txt', 'r')
Lines = file1.readlines()

array_numbers = []

for line in Lines:
    line = line.strip("\n")
    array_numbers.append(int(line))

size_subarray = 25
end_of_loop=False
i=size_subarray
while not end_of_loop:
    if i==len(array_numbers)-1:
        end_of_loop=True
    if not find_sum(array=array_numbers[i-size_subarray:i],item=array_numbers[i]):
        end_of_loop=True
    else:
        i+=1
print("Part 1 result")
print(f"i = {i} -- array_numbers[i]= {array_numbers[i]}")


#Part 2
end_of_loop=False
j=0
while not end_of_loop:
    if j == i:
        end_of_loop=True
        print("Not found")
    else:
        sum_less = True
        suma = 0
        z=j
        while sum_less:
            if z==i:
                sum_less = False
            suma += array_numbers[z]
            if suma == array_numbers[i]:
                print(f"Part 2 result")
                print(f"min(array_numbers[{j}:{z}] : {min(array_numbers[j:z])}")
                print(f"max(array_numbers[{j}:{z}] : {max(array_numbers[j:z])}")
                print(f"min + max : {min(array_numbers[j:z]) + max(array_numbers[j:z])}")
                end_of_loop = True
                sum_less = False
            elif suma > array_numbers[i]:
                sum_less = False
            else:
                z+=1
        j+=1