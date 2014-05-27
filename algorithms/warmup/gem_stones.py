import sys

input_list = [inp for inp in sys.stdin.read().split("\n")]
del input_list[0]


def is_gem(element):
    for member in input_list:
        if element not in member:
            return False
    return True


tested = []
gem_count = 0
for stone in input_list:
    for element in stone:
        if element not in tested:
            if is_gem(element): gem_count = gem_count + 1
            tested.append(element)

print(gem_count)