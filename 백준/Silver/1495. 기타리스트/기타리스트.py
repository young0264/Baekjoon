n, s, m = map(int,input().split())
arr = [0]+list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
# print(dp)
dp[0][s] = 1
#dp의 행은 n의 횟수(주어지는 볼륨), 열은 m의 사이즈
for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j]:
            if 0 <= arr[i]+j <= m:
                dp[i][arr[i]+j] = 1
            if 0 <= j-arr[i] <= m:
                dp[i][j-arr[i]] = 1

for i in range(m,-1,-1):
    if dp[-1][i]:
        print(i)
        exit(0)
print(-1)