n = int(input())
graph = [[] for _ in range(n+1)]    #깊은복사
for _ in range(n):
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-2,2) :
        graph[arr[0]].append((arr[i],arr[i+1]))
def dfs(start):
    visit = [0] * (n + 1)
    stack = [start]
    visit[start] = 1

    while stack:
        next = stack.pop()
        for node in graph[next]:
            if visit[node[0]] == False:
                stack.append(node[0])
                visit[node[0]] = visit[next] + node[1]  #(visit간선누적으로 true처리,),간선의길이
    return visit
#print(dfs(1))

res = dfs(1)
result = dfs(res.index(max(res)))
print(max(result)-1)
