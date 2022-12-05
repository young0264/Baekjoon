#bfs, dp
n,m = map(int,input().split())
graph = []

for i in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)

dp = [[0]*m for _ in range(n)]

dp[0][0] = graph[0][0]

for i in range(1,n):
    dp[i][0] = dp[i-1][0]+graph[i][0]

for i in range(1,m):
    dp[0][i] = dp[0][i-1]+graph[0][i]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+graph[i][j]

print(dp[-1][-1])
# for i in dp:
#     print(i)