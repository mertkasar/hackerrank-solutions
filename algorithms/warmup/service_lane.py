N, M = map(int, input().split())
lane = list(map(int, input().split()))

for i in range(M):
    ent, out = map(int, input().split())
    test = lane[ent:out + 1]
    print(min(test))