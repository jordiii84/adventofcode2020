# import attr

file1 = open('input.txt', 'r')
Lines = file1.readlines()

class Password:
    def __init__(self, max_app, min_app, letter, password):
        self.max_app = max_app
        self.min_app = min_app
        self.letter = letter
        self.password = password


def parse_password(line):
    splitted_password = line.split()
    return Password(
        max_app=splitted_password[0].split("-")[1],
        min_app=splitted_password[0].split("-")[0],
        letter=splitted_password[1].split(":")[0],
        password=splitted_password[2]
    )

count = 0
for line in Lines:
    password = parse_password(line)
    if password.password.count(password.letter) >= int(password.min_app) and password.password.count(password.letter) <= int(password.max_app):
        count += 1

print(f"There are {count} correct passwords with the first rule")

count = 0
for line in Lines:
    password = parse_password(line)
    if (password.password[int(password.min_app)-1] == password.letter) ^ (password.password[int(password.max_app)-1] == password.letter):
        count += 1
print(f"There are {count} correct passwords with the second rule")