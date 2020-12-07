import os
working_dir = os.getcwd()
filename = "data/day3.txt"
#filename = "test.txt"
path = os.path.join(working_dir, filename)

data = []
with open(path) as f:
    for line in f:
        data.append(line.strip())

#### A
xpos = 0
ypos = 0
bottom = len(data)
width = len(data[0])
trees = 0
while (ypos < bottom):
    if (data[ypos][xpos] == "#"):
        trees += 1
    ypos +=1
    xpos = (xpos + 3) % width
print(trees)

#### B
res = 1
y = [1,1,1,1,2]
x = [1,3,5,7,1]
for xp, yp in zip(x,y):
    print (yp,xp)
    trees = 0
    xpos = 0
    ypos = 0
    while (ypos < bottom):
        if (data[ypos][xpos] == "#"):
            trees += 1
        ypos +=yp
        xpos = (xpos + xp) % width
    res *= trees
print(res)




