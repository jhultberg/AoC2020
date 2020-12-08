import os
import copy

current_dir = os.getcwd()
filename = "data/day8.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

instructions = []
with open(path) as f:
    for line in f:
        ins, no = line.split(" ")
        instructions.append((ins.strip(), no.strip()))



def run_program(inst):

    #print(inst)
    excecuted_inst = set()
    accumulator = 0
    idx = 0
    outside = False

    while idx not in excecuted_inst:
        excecuted_inst.add(idx)

        if idx >= len(inst):
            outside = True
            break

        instruction, steps = inst[idx]

        if instruction == "nop":
            idx += 1
        elif instruction == "jmp":
            if steps[0] == "+":
                idx += int(steps[1:])
            else:
                idx -= int(steps[1:])
        elif instruction == "acc":
            if steps[0] == "+":
                accumulator += int(steps[1:])
            else:
                accumulator -= int(steps[1:])
            idx += 1
    return (accumulator, outside)

### A
print(run_program(instructions))


### B
for i in range(len(instructions)):
    modified_instructions = copy.deepcopy(instructions)
    #print(instructions[i][0])
    if instructions[i][0] == "jmp":
        modified_instructions[i] = ("nop", instructions[i][1])
    elif instructions[i][0] == "nop":
        modified_instructions[i] = ("jmp", instructions[i][1])
    #print(modified_instructions[i])
    accumulator, outside = run_program(modified_instructions)
    if(outside):
        print(accumulator)
        break


