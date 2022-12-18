from collections import deque

n , m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []
def topology_sort():
    que = deque()
    for i in range(1,n+1):      ##indegree 0 인값넣고
        if not indegree[i]:
            que.append(i)

    while que:
        now = que.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if not indegree[i]:
                que.append(i)

topology_sort()
print(*result)