class Passport:
    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def is_valid(self):
        return self.is_valid_byr() and self.is_valid_iyr() and self.is_valid_eyr() and self.is_valid_hgt() and self.is_valid_hcl() and self.is_valid_ecl() and self.is_valid_pid() and self.is_valid_cid()

    def is_valid_byr(self):
        return self.byr is not None and self.is_valid_int(self.byr, 1920, 2002)

    def is_valid_iyr(self):
        return self.iyr is not None and self.is_valid_int(self.iyr, 2010, 2020)

    def is_valid_eyr(self):
        return self.eyr is not None and self.is_valid_int(self.eyr, 2020, 2030)

    def is_valid_hgt(self):
        if self.hgt is not None:
            if self.hgt.endswith("in"):
                value = self.hgt.split("in")[0]
                return self.is_valid_int(value, 59, 76)
            elif self.hgt.endswith("cm"):
                value = self.hgt.split("cm")[0]
                return self.is_valid_int(value, 150, 193)
            else:
                return False
        else:
            return False

    def is_valid_hcl(self):
        if self.hcl is not None and self.hcl.startswith("#"):
            return len(self.hcl.split("#")[1]) == 6 and is_hex(self.hcl.split("#")[1])
        else:
            return False

    def is_valid_ecl(self):
        return self.ecl is not None and self.ecl in ["amb","blu","brn","gry","grn","hzl","oth"]

    def is_valid_pid(self):
        if self.pid is not None:
            if len(self.pid) == 9:
                try:
                    int(self.pid)
                    return True
                except Exception:
                    return False
            else:
                return False
        else:
            return False

    def is_valid_cid(self):
        return True

    def is_valid_int(self, value, min_value, max_value):
        return int(value)>= min_value and int(value) <= max_value

def is_hex(s):
    try:
        int(s, 16)
    except ValueError:
        return False
    return len(s) % 2 == 0

def parse_passport(line):
    splitted_passport = line.split(" ")
    passport = Passport()
    for field in splitted_passport:
        splitted_field = field.split(":")
        setattr(passport, splitted_field[0], splitted_field[1])
    return passport

def get_passports(Lines):
    passports = []
    passport = ""
    first=True
    for line in Lines:
        line = line.strip("\n")
        if line == "":
            parsed_passport = parse_passport(passport)
            passports.append(parsed_passport)
            passport=""
            first = True
        else:
            if not first:
                passport += " "
            passport += line
            first = False

    parsed_passport = parse_passport(passport)
    passports.append(parsed_passport)
    return passports


file1 = open('input.txt', 'r')
Lines = file1.readlines()

passports = get_passports(Lines)
valid_passports = 0
for passport in passports:
    if passport.is_valid():
        valid_passports += 1

print(f"There are {valid_passports} valid passports in {len(passports)} passports")