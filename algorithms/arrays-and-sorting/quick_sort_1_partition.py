N = int(input())
inp = list(map(int, input().split()))
P = inp[0]

left, right = [], []
for i in range(1, N):
    if inp[i] < P: left.append(inp[i])
    else: right.append(inp[i])
        
output = left + [P] + right
print(' '.join(str(ch) for ch in output))