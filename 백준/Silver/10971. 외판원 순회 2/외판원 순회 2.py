import sys
n = int(input())
answer = sys.maxsize
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [0]*n
box = []

def dfs(depth,start,sum_value):
    global answer
    if depth == n-1 and graph[start][0] != 0:
        answer = min(answer,sum_value+graph[start][0])
        return
    for i in range(n):
        if not visited[i] and graph[start][i] != 0:
            visited[i] = 1
            dfs(depth+1, i, sum_value + graph[start][i])
            visited[i] = 0

visited[0] = 1
dfs(0,0,0)
print(answer)


#====시간초과====
# def dfs(start,end,cnt):
#     global answer,box
#     if cnt == n and start != end:
#         answer = min(answer,sum(box)+graph[end][start])
#         return
# 
#     for i in range(n):
#         if not visited[i] and end != i:
#             visited[i] = 1
#             box.append(graph[end][i])
#             dfs(start,i,cnt+1)
#             box.pop()
#             visited[i] = 0
# for i in range(n):
#     visited[i] = 1
#     dfs(i,i,1)
#     visited[i] = 0
# print(answer)