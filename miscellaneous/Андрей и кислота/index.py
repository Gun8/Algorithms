n = int(input())
a = list(map(int,input().split()))

def fn(a, n):
    for i in range(n - 1):
        if (a[i+1] - a[i] < 0): 
            return -1
    return a[n - 1] - a[0]

print(fn(a, n))