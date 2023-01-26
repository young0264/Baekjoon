import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, r, q = map(int,input().split())
graph = [[]for _ in range(n+1)]
arr = [[]for _ in range(n+1)]
answer_arr = [1]*(n+1)


for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] += 1
    if graph[x]:
        for nx in graph[x]:
            if not visited[nx]:
                visited[x] += dfs(nx)
                arr[x].append(nx)
    return visited[x]


visited = [0]*(n+1)
dfs(r)


for _ in range(q):
    m = int(input())
    print(visited[m])







