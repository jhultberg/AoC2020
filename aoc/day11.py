import os
import copy

current_dir = os.getcwd()
filename = "data/day11.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

initial_seat_layout = []
with open(path) as f:
    for line in f:
        initial_seat_layout.append(line.strip())


def stable_occupied_seats(seat_layout):
    prev_layout = []
    while seat_layout != prev_layout:
        prev_layout = copy.deepcopy(seat_layout)
        new_layout = []
        for y in range(len(seat_layout)):
            curr_row = seat_layout[y]
            new_row = ""
            for x in range(len(curr_row)):
                startx= max(0, x-1)
                starty= max(0, y-1)
                stopx= min(len(curr_row)-1, x+1)
                stopy= min(len(seat_layout)-1, y+1)
                taken_seats = 0
                for i in range(startx, stopx+1):
                    for j in range(starty, stopy+1):
                        if j == y and i == x:
                            continue
                        if prev_layout[j][i] == "#":
                            taken_seats += 1
                if prev_layout[y][x] == ".":
                    new_row+=prev_layout[y][x]
                elif prev_layout[y][x] == "L" and taken_seats == 0:
                    new_row+="#"
                elif prev_layout[y][x] == "#" and taken_seats >= 4:
                    new_row+="L"
                else:
                    new_row+=prev_layout[y][x]
            new_layout.append(new_row)
        seat_layout = copy.deepcopy(new_layout)

    seats = 0

    for x in range(len(seat_layout)):
        for y in range(len(seat_layout[0])):
            if seat_layout[x][y] == "#":
                seats += 1
    return seats

def find_next_seat_in_dir(seat, seat_map, direction):
    x = seat[0]
    y = seat[1]
    if direction == 0: #left
        x -=1
    elif direction == 1: #up left
        x -=1
        y -=1
    elif direction == 2: #up
        y -=1
    elif direction == 3: #up right
        x +=1
        y -=1
    elif direction == 4: #right
        x +=1
    elif direction == 5: #down right
        x +=1
        y +=1
    elif direction == 6: #down
        y +=1
    elif direction == 7: #down left
        x -=1
        y +=1

    if x < 0 or y < 0 or x > len(seat_map[0])-1 or y > len(seat_map)-1:
        #reached edge
        return False
    if seat_map[y][x] == "#":
        return True
    if seat_map[y][x] == "L":
        return False
    return find_next_seat_in_dir((x,y), seat_map, direction)

def stable_seats(seat_layout):
    prev_layout = []
    while seat_layout != prev_layout:
        prev_layout = copy.deepcopy(seat_layout)
        new_layout = []
        for y in range(len(seat_layout)):
            curr_row = seat_layout[y]
            new_row = ""
            for x in range(len(curr_row)):
                taken_seats = 0
                for direction in range(8):
                    if find_next_seat_in_dir((x,y), seat_layout, direction):
                        taken_seats += 1
                if prev_layout[y][x] == ".":
                    new_row+=prev_layout[y][x]
                elif prev_layout[y][x] == "L" and taken_seats == 0:
                    new_row+="#"
                elif prev_layout[y][x] == "#" and taken_seats >= 5:
                    new_row+="L"
                else:
                    new_row+=prev_layout[y][x]
            new_layout.append(new_row)
        seat_layout = copy.deepcopy(new_layout)

    seats = 0

    for x in range(len(seat_layout)):
        for y in range(len(seat_layout[0])):
            if seat_layout[x][y] == "#":
                seats += 1
    return seats

### A
print(stable_occupied_seats(initial_seat_layout))
### B
print(stable_seats(initial_seat_layout))



