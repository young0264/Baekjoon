import sys
INF = sys.maxsize

n = int(input())

stone_info = [[0,0] for _ in range(n+1)]
dp = [[INF]*(n+1) for _ in range(n+1)]
arr = [0]*(n+1)

for i in range(n-1):
    a, b = map(int,input().split())
    stone_info[i+1][0] = a
    stone_info[i+1][1] = b

k = int(input())
if n==1:
    print(0)
    exit(0)
arr[2] = stone_info[1][0]

for i in range(3,n+1):
    arr[i] = min(arr[i-1]+stone_info[i-1][0], arr[i-2]+stone_info[i-2][1])

for i in range(1,n+1):
    dp[i][i] = arr[i]
    if i+3 <= n :
        dp[i][i+3] = arr[i] + k
    for j in range(i+1,n+1):
        if i <= j-2:
            # dp[i][j] = min(dp[i][j-1]+stone_info[j-1][0], dp[i][j-2]+stone_info[j-2][1])
            dp[i][j] = min(dp[i][j-1]+stone_info[j-1][0], dp[i][j-2]+stone_info[j-2][1],dp[i][j])
        elif i==j-1:
            dp[i][j] = dp[i][j-1] + stone_info[j-1][0]


# for i in range(1,n+1):
answer = INF
for i in range(1,n+1):
    answer = min(dp[i][-1],answer)
print(answer)
