N = int(input())
inp = list(map(int, input().split()))

for i in range(1, N):
    X = inp[i]
    j = i - 1
    
    while j >= 0 and inp[j] > X:
        inp[j+1] = inp[j]
        print(' '.join(str(ch) for ch in inp))
        j = j - 1
    
    inp[j+1] = X
    
print(' '.join(str(ch) for ch in inp))