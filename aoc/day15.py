import os

current_dir = os.getcwd()
filename = "data/day15.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

prog = []
with open(path) as f:
    for line in f:
        numbers = line.split(",")
        prog = [int(x) for x in numbers]


def elf_game(numbers, rounds):
    spoken_numbers = {}
    last_spoken = 0
    first_time = True

    for i, x in enumerate(numbers):
        spoken_numbers[x] = [i]
        last_spoken = x

    for x in range(len(numbers), rounds):
        if first_time:
            last_spoken = 0
            spoken_numbers[last_spoken].append(x)
            first_time = False
            continue
        last_spoken = spoken_numbers[last_spoken][-1] - spoken_numbers[last_spoken][-2]
        if last_spoken not in spoken_numbers:
            first_time = True
            spoken_numbers[last_spoken] = [x]
        else:
            first_time = False
            spoken_numbers[last_spoken].append(x)
    return last_spoken


### A
print(elf_game(prog, 2020))

### B
print(elf_game(prog, 30000000))








