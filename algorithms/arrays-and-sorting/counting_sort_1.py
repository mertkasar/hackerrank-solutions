N = int(input())
input_map = list(map(int, input().split()))
counter = [0] * 100

for element in input_map:
    counter[element] += 1

print(' '.join(str(i) for i in counter))
