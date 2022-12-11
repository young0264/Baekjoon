from itertools import product
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
dp = [[0]*(n+1) for _ in range(31)]

for i in range(1,31):
    dp[i][1] = 1

for i in range(2,31):
    for j in range(2,n+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
print(dp[m][n])
