n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]
dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][0] = i+1
for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = (dp[i-1][j-1])%10007 + (dp[i-1][j])%10007

print((dp[n-1][k-1])%10007)