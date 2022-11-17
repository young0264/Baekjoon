t = int(input())

dp = [[0]*1001 for _ in range(1001)]

dp[1][1] = 1
dp[1][2] = 1
dp[2][2] = 1
dp[1][3] = 1
dp[2][3] = 2
dp[3][3] = 1

# dp[i][j] = i개의 숫자로 숫자j를 만드는 가짓수

for j in range(4,1001):
    for i in range(1,j+1):
        dp[i][j] += dp[i-1][j-1]%1000000009
        dp[i][j] += dp[i-1][j-2]%1000000009
        dp[i][j] += dp[i-1][j-3]%1000000009
for _ in range(t):
    n,m = map(int,input().split())
    print(dp[m][n]%1000000009)