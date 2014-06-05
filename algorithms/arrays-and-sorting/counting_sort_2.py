N = int(input())
input_map = list(map(int, input().split()))
counter = [0] * 100

for element in input_map:
    counter[element] += 1

output = ''
i = 0
while i < 100:
    key = counter[i]
    for j in range(key):
        output = output + str(i) + ' '
    i = i + 1    

print(output)