n, m = map(int, input().split())
n, m = int(n), int(m)

total = 0

for i in range(m):
    a, b, k = map(int, input().split())
    total = total + k * (b - a + 1)

print(int(total / n))