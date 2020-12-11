def get_row(row, to_find):
    row_number=0
    for i in range(len(row)):
        if str(row)[len(row)-1-i] == to_find:
            row_number += 2**i
    return row_number


file1 = open('input.txt', 'r')
Lines = file1.readlines()

higher = 0
list_seats = []
for line in Lines:
    line = line.strip("\n")
    row = get_row(line[0:7], "B")
    column = get_row(line[7:10], "R")
    result = row * 8 + column
    list_seats.append(result)
    if result > higher:
        higher = result

print(f"The higher number is : {higher}")

for seat in list_seats:
    if seat+1 not in list_seats and seat+2 in list_seats:
        print(f"falta el {seat+1}")