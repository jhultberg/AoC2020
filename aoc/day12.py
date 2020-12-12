import os

current_dir = os.getcwd()
filename = "data/day12.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

inst = []
with open(path) as f:
    for line in f:
        inst.append((line[0], int(line[1:].strip())))

def turn(curr_dir, direction, deg):
    directions = []
    if direction == "R":
        directions = ["N", "E", "S", "W"]
    elif direction == "L":
        directions = ["N", "W", "S", "E"]
    new_dir = 0
    if deg == 90:
        new_dir = 1
    elif deg == 180:
        new_dir = 2
    elif deg == 270:
        new_dir = 3
    offset = directions.index(curr_dir)
    new_idx = (new_dir + offset) % 4
    return directions[new_idx]

def turn_waypoint_right(waypoint, deg):
    new_wp = waypoint
    if deg == 90:
        new_wp = (waypoint[1], -waypoint[0])
    elif deg == 180:
        new_wp = (-waypoint[0], -waypoint[1])
    elif deg == 270:
        new_wp = (-waypoint[1], waypoint[0])
    return new_wp

def turn_waypoint_left(waypoint, deg):
    new_wp = waypoint
    if deg == 90:
        new_wp = (-waypoint[1], waypoint[0])
    elif deg == 180:
        new_wp = (-waypoint[0], -waypoint[1])
    elif deg == 270:
        new_wp = (waypoint[1], -waypoint[0])
    return new_wp


def walk(curr_dir, steps, pos):
    if steps == 0:
        return pos
    new_pos = pos
    if curr_dir == "N":
        new_pos = (pos[0], pos[1]+1)
    elif curr_dir == "E":
        new_pos = (pos[0]+1, pos[1])
    elif curr_dir == "S":
        new_pos = (pos[0], pos[1]-1)
    elif curr_dir == "W":
        new_pos = (pos[0]-1, pos[1])
    return(walk(curr_dir, steps - 1, new_pos))

def walk_relative(steps, pos, waypoint):
    return (pos[0] + steps*waypoint[0], pos[1] + steps*waypoint[1])


def follow_instructions(pos, facing_dir, instructions):
    for action, steps in instructions:
        if action == "N":
            pos = walk("N", steps, pos)
        elif action == "S":
            pos = walk("S", steps, pos)
        elif action == "E":
            pos = walk("E", steps, pos)
        elif action == "W":
            pos = walk("W", steps, pos)
        elif action == "L":
            facing_dir = turn(facing_dir, action, steps)
        elif action == "R":
            facing_dir = turn(facing_dir, action, steps)
        elif action == "F":
            pos = walk(facing_dir, steps, pos)
    return pos

def follow_instructions_waypoint(pos, waypoint, instructions):
    for action, steps in instructions:
        if action == "N":
            waypoint = walk("N", steps, waypoint)
        elif action == "S":
            waypoint = walk("S", steps, waypoint)
        elif action == "E":
            waypoint = walk("E", steps, waypoint)
        elif action == "W":
            waypoint = walk("W", steps, waypoint)
        elif action == "L":
            waypoint = turn_waypoint_left(waypoint, steps)
        elif action == "R":
            waypoint = turn_waypoint_right(waypoint, steps)
        elif action == "F":
            pos = walk_relative(steps, pos, waypoint)
    return pos

def manhattan_dist(coord):
    return abs(coord[0]) + abs(coord[1])

waypoint = (10, 1)
ship = (0, 0)
initial_dir = "E"
### A
print(manhattan_dist(follow_instructions(ship, initial_dir, inst)))

### B
print(manhattan_dist(follow_instructions_waypoint(ship, waypoint, inst)))

