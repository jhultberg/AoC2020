import os
from collections import deque

current_dir = os.getcwd()
filename = "data/day9.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

xmas_data = []
with open(path) as f:
    for line in f:
        xmas_data.append(line.strip())

def find_invalid(data):
    preamble = deque(data[:25])
   # print(preamble)
    for val in data[25:]:
        #print(preamble)
        valid = False
        #print(val)
        for i in preamble:
            for j in preamble:
                if int(val) == int(i)+int(j) and int(i) != int(j):
                    #print("valid i ", i, " j ", j)
                    valid = True
                    break
            if valid:
                break
        if  not valid:
            return int(val)
        preamble.append(val)
        preamble.popleft()
    return 0

def find_weakness(data, target_sum):
    not_found = True
    no_to_sum = 2
    vals = deque(data[:no_to_sum])
    while not_found:
        vals = deque(data[:no_to_sum])
        for val in data[no_to_sum:]:
            if sum(int(x) for x in vals) == target_sum:
                not_found = False
                break
            vals.append(val)
            vals.popleft()
        no_to_sum += 1
    return max(int(x) for x in vals) + min(int(x) for x in vals)






### A
print("A: ", find_invalid(xmas_data))

### B

print(find_weakness(xmas_data, find_invalid(xmas_data)))
