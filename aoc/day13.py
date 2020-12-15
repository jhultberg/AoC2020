import os
import math

current_dir = os.getcwd()
filename = "data/day13.txt"
#filename = "test.txt"

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

def buses_and_offsets(all_buses):
    idx = -1
    bus_offset = []
    for bus in all_buses:
        idx +=1
        if bus == "x":
            continue
        bus_offset.append((int(bus), idx))
    return bus_offset

def earliest_for_all_buses(buses):
    time = 0
    W = int(buses[0][0])
    for bus in buses[1:]:
        idx = int(bus[1])
        while (time + idx) % int(bus[0]) != 0:
            time += W
        W *= int(bus[0])
    return time

### A
print(waitingtime(earliest_bus_after_timestamp(all_buses, earliest_time), earliest_time))

### B
print(earliest_for_all_buses(buses_and_offsets(all_buses)))
