import os
import re

working_dir = os.getcwd()
filename = "data/day4.txt"
#filename = "test.txt"
path = os.path.join(working_dir, filename)

data = []
with open(path) as f:
    for line in f:
        data.append(line.strip())

passports = []

curr = ""
for i in range(len(data)):
    line = data[i]
    if  line == "":
        passports.append(curr.strip())
        curr = ""
        continue

    curr = curr + line.strip() + " "
    if (i == len(data)-1):
        passports.append(curr.strip())

valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

#print(passports)

no_valid_passports = 0
valid_passports = []

for passport in passports:
    fields = passport.split(" ")
    present_fields = []
    for field in fields:
        present_fields.append(field.split(":")[0])

    valid = True
    for f in valid_fields:
        if f not in present_fields:
            if f != "cid":
                valid = False
    if valid:
        no_valid_passports += 1
        valid_passports.append(passport)
print(no_valid_passports)
print(len(valid_passports))


no_valid_passports = 0
for passport in valid_passports:
    valid = True
    fields = passport.split(" ")
    for field in fields:
        typ, val = field.split(":")
        if typ == "byr":
            valid = 1920 <= int(val) <= 2002
        elif typ == "iyr":
            valid = 2010 <= int(val) <= 2020
        elif typ == "eyr":
            valid = 2020 <= int(val) <= 2030
        elif typ == "hgt":
            meas = val[-2:]
            if meas == "cm":
                valid = 150 <= int(val[:-2]) <= 193
            elif meas == "in":
                valid = 59 <= int(val[:-2]) <= 76
            else:
                valid = False
        elif typ == "hcl":
            if not re.match("#[a-f0-9]{6}", val):
                valid = False
        elif typ == "ecl":
            valid = val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif typ == "pid":
            if not re.match("\d{9}", val):
                valid = False
            else:
                valid = len(val) == 9

        if not valid:
            break
    print(passport, valid)
    if valid:
        no_valid_passports += 1

print(no_valid_passports)
