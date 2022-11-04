n = int(input())

dp = [[0]*10 for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1
    dp[2][i] = 10-i

for i in range(3, 1001):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])
# print(dp[3])
print(sum(dp[n])%10007)