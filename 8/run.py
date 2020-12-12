def parse_action(action):
    splitted_action = action.split(" ")
    return splitted_action

file1 = open('input.txt', 'r')
Lines = file1.readlines()

program_ended = False
reverse_index=0

while not program_ended:
    loop_found=False
    position = 0
    accumulate = 0
    visited_positions=[]
    reversable_items=0

    while not loop_found and not program_ended:
        if position == len(Lines)-1:
            program_ended = True

        elif position not in visited_positions:
            visited_positions.append(position)
            action = parse_action(Lines[position].strip("\n"))
            if action[0]=="nop":
                if reverse_index==reversable_items:
                    position+=int(action[1])
                else:
                    position+=1
                reversable_items+=1

            elif action[0]=="jmp":
                if reverse_index==reversable_items:
                    position+=1
                else:
                    position+=int(action[1])
                reversable_items+=1
            elif action[0]=="acc":
                position+=1
                accumulate+=int(action[1])
        else:
            loop_found=True

    reverse_index+=1

print(f"Program ended? {program_ended}")
print(f"Found loop? {loop_found}")
print(f"Accumulate = {accumulate}")



