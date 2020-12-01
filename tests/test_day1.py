from aoc.day1 import two, three, solve

test_data = [1721, 979, 366, 299, 675, 1456]

def test_two():
    assert two(test_data) == 514579


def test_three():
    assert three(test_data) == 241861950


def test_solve():
    assert solve("data/day1.txt") == (211899, 275765682)
