import os

current_dir = os.getcwd()
filename = "data/day10.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

all_jolts = []
with open(path) as f:
    for line in f:
        all_jolts.append(int(line.strip()))
all_jolts.sort()

def count_jolt_differences(jolts):
    device_jolt = jolts[-1]
    current_jolt = 0

    not_connected = True
    ones = 0
    threes = 0
    while not_connected:
        if current_jolt == device_jolt:
            not_connected = False
            threes += 1
            return ones * threes
        if jolts[0] - current_jolt == 1:
            ones += 1
            current_jolt = jolts[0]
            jolts = jolts[1:]
        elif jolts[0] - current_jolt == 3:
            threes += 1
            current_jolt = jolts[0]
            jolts = jolts[1:]
    return 0

def find_sections(jolts):
    sections = []
    curr_section = []
    for jolt in jolts:
        if ((jolt+1 in jolts) != (jolt+2 in jolts)) != ((jolt+2 in jolts) != (jolt+3 in jolts)):
            curr_section.append(jolt)
            sections.append(curr_section)
            print(curr_section)
            curr_section = []
            continue
        curr_section.append(jolt)
    sections.append(curr_section)
    return sections


#def find_all_paths(jolts):
#    no_paths = 1
#    for jolt in jolts[1:]:
#        local_paths = 0
#        if jolt - 1 in jolts:
#            local_paths += 1
#        if jolt - 2 in jolts:
#            local_paths += 1
#        if jolt - 3 in jolts:
#            local_paths += 1
#        no_paths *= local_paths
#    return no_paths


def find_all_paths(jolts):
    ways_to = {0:1}
    for jolt in jolts:
        local_paths = 0
        for x in range(1,4):
            if (jolt-x) in ways_to:
                local_paths += ways_to[jolt-x]
        ways_to[jolt] = local_paths

    return ways_to[jolts[-1]]



### A
print(count_jolt_differences(all_jolts))

### B
print(find_all_paths(all_jolts))

