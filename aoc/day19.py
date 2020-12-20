import os
import re

current_dir = os.getcwd()
filename = "data/day19.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

prog = []
with open(path) as f:
    for line in f:
        prog.append(line.strip())

all_rules = []
part =[]
for p in prog:
    if p == "":
        all_rules = part
        part = []
        continue
    part.append(p)
messages = part

rules = {}
for rule in all_rules:
    val, cond = rule.split(": ")
    rules[val] = cond.replace("\"", "")

def follow_rule(rules, rule_nr):
    sub_rules = rules[rule_nr]
    sub_rules = sub_rules.split("\|")
    for sr in sub_rules:
        new_rules = sr.split(" ")
        for nr in new_rules:
            if re.search(r'[a-z]', nr):
                return nr
            else:
                 return follow_rule(rules, nr)

print(follow_rule(rules, "0"))
