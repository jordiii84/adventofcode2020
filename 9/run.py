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
while not end_of_loop:
    for i in range(size_subarray, len(array_numbers)-1):
        if not find_sum(array=array_numbers[i-size_subarray:i],item=array_numbers[i]):
            print(f"i = {array_numbers[i]}")
            end_of_loop=True
