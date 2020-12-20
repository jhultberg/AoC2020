import os
import math

current_dir = os.getcwd()
#filename = "data/day20.txt"
filename = "test.txt"

path = os.path.join(current_dir, filename)

prog = []
with open(path) as f:
    for line in f:
        prog.append(line.strip())

#print(prog)

ID = 0
grids = {}
top = False
left = ""
right = ""
last_line = ""
for line in prog:
    if "Tile" in line:
        ID = int(line.split(" ")[1][:-1])
        grids[ID] = []
        top = True
        continue
    elif top:
        grids[ID].append(line)
        top = False
    elif line == "":
        grids[ID].append(left)
        grids[ID].append(right)
        grids[ID].append(last_line)
        left = ""
        right = ""
        ID = 0
        continue
    left += line[0]
    right += line[-1]
    last_line = line

grids[ID].append(left)
grids[ID].append(right)
grids[ID].append(last_line)
print(grids)
size = int(math.sqrt(len(grids)))


