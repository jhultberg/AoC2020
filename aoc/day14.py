import os
import re
import itertools

current_dir = os.getcwd()
filename = "data/day14.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

prog = []
with open(path) as f:
    for line in f:
        instruction, value = line.split(" = ")
        prog.append((instruction, value.strip()))

def execute_program(program):
    size = 36
    mask = ""
    memory = {}
    for instruction, value in program:
        if instruction == "mask":
            mask = value
            continue
        address = re.search(r'mem\[(\d*)\]', instruction).group(1)
        val_to_write = bin(int(value))[2:].zfill(size)

        final_value = ""
        for idx, c in enumerate(str(mask)):
            if c == "X":
                final_value += val_to_write[idx]
                continue
            final_value += c
        memory[address] = int(final_value, 2)
    return memory

def sum_memory(memory):
    return sum(int(x) for x in memory.values())

def all_addresses(address, mask):
    all_x =[i for i, a in enumerate(mask) if a == "X"]
    all_1 =[i for i, a in enumerate(mask) if a == "1"]
    combinations = list(itertools.product([0,1], repeat=len(all_x)))
    addresses = []
    for comb in combinations:
        new_address = ""
        replaced = 0
        for i, c in enumerate(address):
            if i in all_1:
                new_address += "1"
            elif i in all_x:
                new_address += str(comb[replaced])
                replaced += 1
            else:
                new_address += c
        addresses.append(new_address)
    return addresses


def ver2_chip(program):
    size = 36
    mask = ""
    memory = {}
    for instruction, value in program:
        if instruction == "mask":
            mask = value
            continue
        address = re.search(r'mem\[(\d*)\]', instruction).group(1)
        addresses = all_addresses(bin(int(address))[2:].zfill(size), mask)
        for a in addresses:
            memory[int(a,2)] = value
    return memory


### A
print(sum_memory(execute_program(prog)))

### B
print(sum_memory(ver2_chip(prog)))
