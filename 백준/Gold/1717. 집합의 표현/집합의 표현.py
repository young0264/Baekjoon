import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [i for i in range(n+1)]

def find_parent(x):
    if arr[x] == x:
        return x
    arr[x] = find_parent(arr[x])
    return arr[x]

def union(a,b):
    x = find_parent(a)
    y = find_parent(b)
    if x==y:
        return
    arr[x] = y
    return

for i in range(m):
    k, a, b = map(int,input().split())
    if k == 0:
        union(a,b)
    else:
        resa,resb = find_parent(a), find_parent(b)
        if resa == resb:
            print("YES")
        else:
            print("NO")


