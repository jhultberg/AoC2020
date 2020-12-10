import os
import string

current_dir = os.getcwd()
#filename = "test.txt"
filename = "data/day6.txt"

path = os.path.join(current_dir, filename)

data = []
with open(path) as f:
    for line in f:
        data.append(line.strip())

### A
group = set()
total_sum = 0
for line in data:
    if line == "":
        total_sum += len(group)
        group = set()
        continue

    for c in line:
        group.add(c)
total_sum += len(group)
print(total_sum)


### B
letters = set(string.ascii_lowercase)
group = set()
total_sum = 0
prev_line = ""
for line in data:
    #print(line, group, total_sum)
    if line == "":
        #print("length: ", len(group))
        total_sum += len(group)
        letters = set(string.ascii_lowercase)
        group = set()
        prev_line = line
        continue

    if (len(group) == 0 and prev_line == ""):
        for c in line:
            group.add(c)
        prev_line = line
        continue

    curr_line = set(list(line))
    tmp = group.intersection(curr_line)
    group = tmp
    prev_line = line

total_sum += len(group)
print(total_sum)

