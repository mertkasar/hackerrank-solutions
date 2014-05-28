t = int(input())

for i in range(t):
    n, c, m = map(int, input().split())

    amount = int(n / c)
    wrappers = amount

    while wrappers >= m:
        wrappers -= m - 1
        amount += 1

    print(amount)