import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * n
answer = 0


def dfs(start, depth):
    global answer
    if depth == 4:
        answer = 1
        return
    # for i in graph[start]:
    for i in graph[start]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth + 1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0
print(answer)
