t = int(input())
dp = [[0]*10001 for _ in range(4)]
for i in range(1,10001):
    dp[1][i] = 1

dp[2][2] = 1
dp[2][3] = 1
dp[3][3] = 1

for i in range(4,10001):
    dp[2][i] = dp[1][i-2] + dp[2][i-2]
    dp[3][i] = dp[1][i-3] + dp[2][i-3] + dp[3][i-3]

for _ in range(t):
    n = int(input())
    print(dp[1][n]+dp[2][n]+dp[3][n])

