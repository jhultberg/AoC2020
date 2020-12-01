def two(data):
    for i in data:
        for j in data:
            if i+j == 2020
                return i*j
    return 0

def three(data):
    for i in data:
        for j in data:
            for k in data:
                if i+j+k == 2020
                   return i*j*k
    return 0


def solve(path):
    with open(path) as ins:
        data = ins.readlines()
        a = two(data)
        b = three(data)
        return (a, b)
