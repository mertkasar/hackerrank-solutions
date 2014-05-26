import sys

def growth(cycle):
    height = 1

    for i in range(1, cycle + 1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2

    return height


input_list = [int(imp) for imp in sys.stdin.read().split('\n')]
del input_list[0]

for i in input_list:
    print(growth(i))
