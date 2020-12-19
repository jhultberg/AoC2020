import os
import math

current_dir = os.getcwd()
filename = "data/day18.txt"
#filename = "test.txt"

path = os.path.join(current_dir, filename)

prog = []
with open(path) as f:
    for line in f:
        prog.append(line.strip().replace(" ", ""))


def basic_calculation(calculation):
    res = 0
    symbol = "+"
    parenthesis = ""
    no_par = 0
    for c in calculation:
        if no_par != 0:
            parenthesis += c
            if c == "(":
                no_par +=1
            elif c == ")":
                no_par -= 1
            if no_par == 0:
                term = basic_calculation(parenthesis[1:-1])
                if symbol == "+":
                    res += term
                elif symbol == "*":
                    res *= term
                parenthesis = ""
        else:
            if c == "(":
                no_par +=1
                parenthesis += c
            elif c == "+" or c == "*":
                symbol = c
            else:
                if symbol == "+":
                    res += int(c)
                elif symbol == "*":
                    res *= int(c)
    return res

def add(vals):
    return sum([int(x) for x in vals.split("+")])

def new_calculation(calculation):
    if "(" not in calculation and ")" not in calculation:
        terms = calculation.split("*")
        return math.prod([add(x) for x in terms])
    parenthesis = ""
    no_par = 0
    simplified_calc = ""
    for c in calculation:
        if no_par != 0:
            parenthesis += c
            if c == "(":
                no_par +=1
            elif c == ")":
                no_par -= 1
            if no_par == 0:
                simplified_calc += str(new_calculation(parenthesis[1:-1]))
                parenthesis = ""
        else:
            if c == "(":
                no_par +=1
                parenthesis += c
            else:
                simplified_calc += c
    return new_calculation(simplified_calc)


### A
### B
tot_sum_A = 0
tot_sum_B = 0
for calculation in prog:
    tot_sum_A += basic_calculation(calculation)
    tot_sum_B += new_calculation(calculation)
print(tot_sum_A, tot_sum_B)
