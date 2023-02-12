n,m = map(int,input().split())
graph = []
A = []
B = []
for _ in range(n):
    arr = list(map(int,input().split()))
    A.append(arr)

for _ in range(n):
    arr = list(map(int,input().split()))
    B.append(arr)

for i in range(n):
    res = [0]*m
    for j in range(m):
        res[j] = A[i][j]+B[i][j]
    print(*res)