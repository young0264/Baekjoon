t = int(input())
dp = [[0] * 100001 for _ in range(4)]
for i in range(1, 100001):
    dp[1][i] = 1
dp[2][2] = 1
dp[3][3] = 1
dp[2][4], dp[1][4] = 1,2
dp[2][5] = 1
dp[1][5] = 2
dp[1][6] = 3
dp[2][6] = 2
dp[3][6] = 1
for i in range(7, 100001):
    dp[1][i] = (dp[1][i - 2] + dp[2][i - 2] + dp[3][i - 2])%1000000009
    dp[2][i] = (dp[1][i - 4] + dp[2][i - 4] + dp[3][i - 4])%1000000009
    dp[3][i] = (dp[1][i - 6] + dp[2][i - 6] + dp[3][i - 6])%1000000009
for _ in range(t):
    n = int(input())
    print((dp[1][n] + dp[2][n] + dp[3][n])%1000000009)