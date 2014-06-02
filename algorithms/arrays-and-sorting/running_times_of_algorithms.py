N = int(input())
inp = list(map(int, input().split()))

counter = 0

for i in range(1, N):
    j = i    
    while j > 0 and inp[j-1] > inp[j]:        
        inp[j], inp[j-1] = inp[j-1], inp[j] 
        j = j - 1
        counter = counter + 1
        
print(counter)