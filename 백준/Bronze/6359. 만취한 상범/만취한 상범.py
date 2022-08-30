t = int(input())
dp = [[0]*101 for _ in range(101)]

#
for i in range(2,101):
    for j in range(2,101):
        if j%i == 0:
            if dp[i-1][j]==1 :
                dp[i][j] = 0
            elif dp[i-1][j] == 0:
                dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j]


for _ in range(t):
    answer=0
    n = int(input())
    for i in range(1,n+1):
        if dp[n][i]==0:
            answer += 1
    print(answer)

