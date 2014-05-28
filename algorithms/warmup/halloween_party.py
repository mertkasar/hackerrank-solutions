import sys

input_list = [int(inp) for inp in sys.stdin.read().split("\n")]
del input_list[0]

def piece(cuts):
    if cuts % 2 == 0:
        return int((cuts / 2) ** 2)
    else:
        horizontal = (cuts + 1) / 2
        vertical = cuts - horizontal
        return int(horizontal * vertical)

for cut in input_list:
    print(piece(cut))