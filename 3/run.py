def count_trees(jump_right, jump_down, log=False):
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    count_trees = 0
    j=0
    for i in range(len(Lines)):
        line = Lines[i].strip("\n")
        if (i%jump_down)==0:
            if line[(j*jump_right)%len(line)] == "#":
                count_trees += 1

            j += 1
    return count_trees



print(f"The plane has crashed with {count_trees(1,1, False)}")
print(f"The plane has crashed with {count_trees(3,1, False)}")
print(f"The plane has crashed with {count_trees(5,1, False)}")
print(f"The plane has crashed with {count_trees(7,1, False)}")
print(f"The plane has crashed with {count_trees(1,2, False)}")

print(f"Result: {count_trees(1,1) * count_trees(3,1) * count_trees(5,1) * count_trees(7,1) * count_trees(1,2)} ")