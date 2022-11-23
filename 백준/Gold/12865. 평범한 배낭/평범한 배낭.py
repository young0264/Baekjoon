# 반례
# 5 10
# 3 8
# 4 7
# 1 9
# 5 6
# 2 1

n, k = map(int,input().split())

dp =[[0]*(100001) for _ in range(101)]
arr = []

for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
    dp[i+1][w] = v

for i in range(1, n+1):
    w, v = arr[i-1]
    for j in range(k+1):
        if j <= w:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])


# for i in dp:
#     print(*i)