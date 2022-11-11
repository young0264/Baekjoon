import sys
sys.setrecursionlimit(10**5)
n = int(input())
arr = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = (map(int, input().split()))
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (n + 1)
visited[0] = 1
visited[1] = 1

answer = 0


def dfs(x):
    global answer
    flag = 0
    
    for nx in arr[x]:
        if not visited[nx]:
            flag = 1
            visited[nx] = visited[x] + 1

            dfs(nx)
    if not flag:
        answer += visited[x]-1
        return
dfs(1)
# print(answer)

if answer % 2 == 0:
    print('No')
else:
    print('Yes')