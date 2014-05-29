N, K = int(input()), int(input())
I = [int(input()) for i in range(N)]

I.sort()

m = I[-1] - I[0] #get maximum unfairness
for i in range(N-K+1):
    '''for every ith block consisting K element in array,
    test it with previous value of m '''
    m = min(m, I[i+K-1]-I[i])
print(m)