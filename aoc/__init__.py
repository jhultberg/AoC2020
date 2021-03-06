import sys

from . import (
        day1,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: aoc <day> [args...]")
        exit(0)

    day = int(sys.argv[1])
    if day == 1:
        a, b = day1.solve(sys.argv[2])
    else:
        print("No solution for the given day ({})".format(day))
        exit(1)

    print("A:", a)
    if b is not None:
        print("B:", b)

