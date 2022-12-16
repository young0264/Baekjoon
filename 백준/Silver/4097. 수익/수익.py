import sys

while True:
    t = int(input())
    if t==0:
        exit(0)
    INF = -sys.maxsize
    dp = [INF]*t
    if t == 0:
        break
    for i in range(t):
        n = int(input())
        if i==0:
            dp[0] = n
        else:
            dp[i] = max(n,dp[i-1]+n)
    answer = max(dp)
    print(answer)