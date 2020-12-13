import os
import math

current_dir = os.getcwd()
#filename = "data/day13.txt"
filename = "test.txt"

path = os.path.join(current_dir, filename)

data = []
with open(path) as f:
    for line in f:
        data.append(line.strip())

earliest_time = int(data[0])
all_buses = data[1].split(",")

def earliest_bus_after_timestamp(buses, earliest_timestamp):
    best_bus = (0, float("inf"))
    for bus in buses:
        if bus == "x":
            continue
        if earliest_timestamp/int(bus) < best_bus[1]:
            best_bus = (int(bus), earliest_timestamp/int(bus))
    print(best_bus)
    return best_bus[0]

def waitingtime(bus, earliest_timestamp):
    return (bus*math.ceil(earliest_timestamp/bus) - earliest_timestamp)*bus

### A
print(waitingtime(earliest_bus_after_timestamp(all_buses, earliest_time), earliest_time))

### B
idx = -1
bus_offset = []
for bus in all_buses:
    idx +=1
    if bus == "x":
        continue
    bus_offset.append((int(bus), idx))
print(bus_offset)

target = 0
multiple = bus_offset[0][0]
for bus in bus_offset[1:]:
    idx = 1
    while not (idx * multiple) % bus[0] == bus[0] - bus[1]:
        idx += 1
    target = multiple * idx
    print(target, idx)
print(target)

