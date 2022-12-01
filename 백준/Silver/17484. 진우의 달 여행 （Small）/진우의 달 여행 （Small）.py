import sys
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 1,2,3
dp = [[[sys.maxsize]*3 for _ in range(m)] for _ in range(n)]
for j in range(m):
    dp[0][j][0] = graph[0][j]
    dp[0][j][1] = graph[0][j]
    dp[0][j][2] = graph[0][j]
#not 0
for i in range(1,n):
    for j in range(m):
        if j==0:
            dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + graph[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][0],dp[i-1][j+1][1]) + graph[i][j]
        elif j==m-1:
            dp[i][j][0] = min(dp[i-1][j-1][1],dp[i-1][j-1][2]) + graph[i][j]
            dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + graph[i][j]
        else:
            dp[i][j][0] = min(dp[i-1][j-1][1],dp[i-1][j-1][2]) + graph[i][j]
            dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + graph[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][0],dp[i-1][j+1][1]) + graph[i][j]
answer = sys.maxsize
for j in range(m):
    answer = min(answer, min(dp[-1][j]))
print(answer)
