import sys
input = sys.stdin.readline
t = int(input())
dp = [[ [0]*2 for _ in range(100001) ] for _ in range(4)]

# print(dp[3][80][1]) # 행열, 홀짝

dp[1][1][0] = 1
dp[1][2][1] = 1
dp[2][2][0] = 1

dp[1][3][0] = 1
dp[1][3][1] = 1

dp[2][3][1] = 1
dp[3][3][0] = 1
for j in range(4,100001):
    for i in range(1,4):
        # if i==1:
        dp[1][j][0] += dp[i][j-1][1]%1000000009
        dp[1][j][1] += dp[i][j-1][0]%1000000009

        dp[2][j][0] += dp[i][j-2][1]%1000000009
        dp[2][j][1] += dp[i][j-2][0]%1000000009

        dp[3][j][0] += dp[i][j-3][1]%1000000009
        dp[3][j][1] += dp[i][j-3][0]%1000000009

        # elif i==2:
        #     dp[i][j][0] += dp[i][j - 2][1]
        #     dp[i][j][1] += dp[i][j - 2][0]
        # else:
        #     dp[i][j][0] += dp[i][j - 3][1]
        #     dp[i][j][1] += dp[i][j - 3][0]
for _ in range(t):
    n = int(input())
    a = (dp[1][n][0] + dp[2][n][0] + dp[3][n][0])%1000000009
    b = (dp[1][n][1] + dp[2][n][1] + dp[3][n][1])%1000000009

    print(a, b)





