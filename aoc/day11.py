import os
import copy

current_dir = os.getcwd()
#filename = "data/day11.txt"
filename = "test.txt"

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
    #print(prev_layout)
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

### A
print(stable_occupied_seats(initial_seat_layout))

### B

