N = int(input())
inp = list(map(int, input().split()))

def sort(arr):
    if len(arr) == 0 or len(arr) == 1: return arr
    
    P = arr[0]
    
    left = [i for i in arr if i < P]
    right = [i for i in arr if i > P]
     
    output = sort(left) + [P] + sort(right)
    print(" ".join(str(i) for i in output))
    return output

sort(inp)