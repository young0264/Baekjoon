n = int(input())
m = int(input())
graph = [[] for _ in range(n + 2)]
#visit=[]
visit_stack=[]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited=[]
    need_visit=[]
    need_visit.append(start)
    while need_visit:
        node = need_visit.pop()
        if node not in visited :
            visited.append(node)
            for i in graph[node]:
                need_visit.append(i)
    return visited

print(len(dfs(1))-1)





