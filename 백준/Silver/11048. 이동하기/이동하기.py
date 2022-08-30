r,c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
dp = [[0]*c for _ in range(r)]
dp[0][0] = graph[0][0]
for i in range(1,r):
    dp[i][0] = dp[i-1][0] + graph[i][0]
for i in range(1,c):
    dp[0][i] = dp[0][i-1] + graph[0][i]

for i in range(1,r):
    for j in range(1,c):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + graph[i][j]

print(dp[-1][-1])