n = int(input())
m = int(input())
arr = []
for _ in range(m):
    a, b, d, = list(map(int, input().split()))
    arr.append((d, a, b))
arr = sorted(arr, key=lambda x: x[0])
parent = [i for i in range(n + 1)]
answer = 0


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    na, nb = find(a), find(b)
    if na > nb:
        parent[na] = nb
    else:
        parent[nb] = na

for dist, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        answer += dist
    # print(1)
print(answer)
