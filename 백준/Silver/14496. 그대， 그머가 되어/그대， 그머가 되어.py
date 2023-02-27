from collections import deque
import sys
start, end = map(int,input().split())
n,m = map(int,input().split())
INF = sys.maxsize
answer = INF
visited = [0]*(n+1)
arr = [[] for _ in range(n+1)]
if start == end:
    print(0)
    exit(0)
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

que = deque()
que.append(start)
while que:
    dx = que.popleft()
    for nx in arr[dx]:
        if not visited[nx]:
            visited[nx] = visited[dx] + 1
            que.append(nx)

if not visited[end]:
    print(-1)
else :
    print(visited[end])

