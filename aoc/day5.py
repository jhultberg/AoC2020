import os

def find_seat_id(bpass):
#    print(bpass)
    rows = list(range(no_rows))
    row_id = 0
    seat = 0
    for b in bpass[:7]:
        n = int(len(rows) / 2)
        if b == "F":
            tmp = rows[:n]
            rows = tmp
        elif b == "B":
            tmp = rows[n:]
            rows = tmp
        if len(rows) == 1:
            row_id = rows[0]
            #print(row_id)
            break

    seats = list(range(no_cols))
    for b in bpass[7:]:
        n = int(len(seats) / 2)
        if b == "L":
            tmp = seats[:n]
            seats = tmp
        elif b == "R":
            tmp = seats[n:]
            seats = tmp
        if len(seats) == 1:
            seat = seats[0]
            #print(seat)
            break

    return row_id *8 + seat

#########################################

no_rows = 128
no_cols = 8

current_dir = os.getcwd()
#filename = "test.txt"
filename = "data/day5.txt"

path = os.path.join(current_dir, filename)

data = []
with open(path) as f:
    for line in f:
        data.append(line.strip())

### A
highest_id = 0

for bpass in data:
    seat_id = find_seat_id(bpass)
    if seat_id > highest_id:
        highest_id = seat_id
print(highest_id)

### B
all_ids = []
for bpass in data:
    all_ids.append(find_seat_id(bpass))
all_ids.sort()
for idx in all_ids:
    if idx - 1 in all_ids and idx + 1 in all_ids:
        continue
    if all_ids.index(idx) == 0 or all_ids.index(idx) == len(all_ids) - 1:
        continue
    print(idx)
