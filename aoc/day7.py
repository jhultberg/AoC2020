import os
import re


def find_bags(all_bags, current_bag, my_bag):
    contents = all_bags[current_bag]
    #print(current_bag, contents)
    if contents == {}:
        return False
    if my_bag in contents:
        return True
    can_hold = False
    for bag in contents:
        can_hold = find_bags(all_bags, bag, my_bag) or can_hold
    return can_hold


def count_bags(all_bags, current_bag):
    contents = all_bags[current_bag]
    #print(current_bag, contents)
    if contents == {}:
        return 0
    no_bags = 0
    for bag, count in contents.items():
        no_bags += int(count) + int(count) * count_bags(all_bags, bag)
    return no_bags








current_dir = os.getcwd()
#filename = "data/day7.txt"
filename = "test.txt"

path = os.path.join(current_dir, filename)

data = []
with open(path) as f:
    for line in f:
        data.append(line.strip())

bags = {}
for line in data:
    bag, content = line.split(" bags contain ")
    if bag not in bags:
        if content == "no other bags.":
            bags[bag] = {}
            continue
        contains = {}
        for c in content.split(", "):
            bag_type = re.sub(r'\sbags?\.?', "", c)
            contains[bag_type[2:]] = bag_type[0]
        bags[bag] = contains
#print(len(bags), bags)

my_bag = "shiny gold"

### A
tot = 0
for bag in bags:
    if find_bags(bags, bag, my_bag):
        tot += 1
print(tot)

### B
bags_inside = count_bags(bags, my_bag)
print(bags_inside)
