import os
import copy

current_dir = os.getcwd()
filename = "data/day17.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

prog = []
with open(path) as f:
    for line in f:
        prog.append(line.strip())

def add_z(state, xdim, ydim, zdim):
    for i in range(xdim[0]-1, xdim[1]+2):
        for j in range(ydim[0]-1, ydim[1]+2):
            for k in [zdim[0]-1, zdim[1]+1]:
                state[(i,j,k)] = False
    return state

def expand(state, xdim, ydim,zdim):
    new_state = copy.deepcopy(state)
    for i in range(xdim[0]-1, xdim[1]+2):
        for j in range(ydim[0]-1, ydim[1]+2):
            for k in range(zdim[0], zdim[1]+1):
                if (i,j,k) not in new_state:
                    new_state[(i,j,k)]=False
    return new_state

def initial_setup(src):
    state = {}
    line = 0
    for pos in src:
        for i, c in enumerate(pos):
            status = c == "#"
            state[(i, line, 0)] = status
        line += 1
    return state

def active_neighbors(state, coord):
    neighbors =0
    for pos in state:
        if pos[0] in range(coord[0] -1, coord[0]+2) and pos[1] in range(coord[1] -1, coord[1]+2) and pos[2] in range(coord[2] -1, coord[2]+2):
            if pos[0] == coord[0] and pos[1] == coord[1] and pos[2] == coord[2]:
                continue
            if state[pos]:
                neighbors += 1
    return neighbors


def update_state(state):
    new_state = {}
    for coord in state:
        new_state[coord] = state[coord]
        no_active_neighbors = active_neighbors(state, coord)
        if  state[coord] and no_active_neighbors not in [2,3]:
            new_state[coord] = False
        elif not state[coord] and no_active_neighbors == 3:
            new_state[coord] = True
    return new_state

def dim(coords):
    return (min(coords), max(coords))

def run_cycles(state, cycles):
    for i in range(1,cycles+1):
        xdim = dim([x[0] for x in state])
        ydim = dim([x[1] for x in state])
        zdim = dim([x[2] for x in state])

        state = expand(copy.deepcopy(state), xdim, ydim, zdim)
        state = add_z(copy.deepcopy(state), xdim, ydim, zdim)
        state = update_state(copy.deepcopy(state))
        active = 0
        for coord in state:
            if state[coord]:
                active += 1
    return active

#---------------------------------------------

def expand_4(state, xdim, ydim,zdim, wdim):
    new_state = copy.deepcopy(state)
    for i in range(xdim[0]-1, xdim[1]+2):
        for j in range(ydim[0]-1, ydim[1]+2):
            for k in range(zdim[0]-1, zdim[1]+2):
                for l in range(wdim[0]-1, wdim[1]+2):
                    if (i,j,k,l) not in new_state:
                        new_state[(i,j,k, l)]=False
    return new_state

def initial_setup_4(src):
    state = {}
    line = 0
    for pos in src:
        for i, c in enumerate(pos):
            status = c == "#"
            state[(i, line, 0, 0)] = status
        line += 1
    return state

def active_neighbors_4(state, coord):
    neighbors =0
    for pos in state:
        if pos[0] in range(coord[0] -1, coord[0]+2) and pos[1] in range(coord[1] -1, coord[1]+2) and pos[2] in range(coord[2] -1, coord[2]+2) and pos[3] in range(coord[3] -1, coord[3]+2):
            if pos[0] == coord[0] and pos[1] == coord[1] and pos[2] == coord[2] and pos[3] == coord[3]:
                continue
            if state[pos]:
                neighbors += 1
    return neighbors


def update_state_4(state):
    new_state = {}
    for coord in state:
        new_state[coord] = state[coord]
        no_active_neighbors = active_neighbors_4(state, coord)
        if  state[coord] and no_active_neighbors not in [2,3]:
            new_state[coord] = False
        elif not state[coord] and no_active_neighbors == 3:
            new_state[coord] = True
    return new_state

def run_cycles_4(state, cycles):
    for i in range(1,cycles+1):
        xdim = dim([x[0] for x in state])
        ydim = dim([x[1] for x in state])
        zdim = dim([x[2] for x in state])
        wdim = dim([x[3] for x in state])

        state = expand_4(copy.deepcopy(state), xdim, ydim, zdim, wdim)
        state = update_state_4(copy.deepcopy(state))
        active = 0
        for coord in state:
            if state[coord]:
                active += 1
    return active
### A
state = initial_setup(prog)
print(run_cycles(state, 6))

### B
state4 = initial_setup_4(prog)
print(run_cycles_4(state4, 6))

