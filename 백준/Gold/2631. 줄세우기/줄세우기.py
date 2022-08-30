n = int(input())
arr = []
dp = [1]*n

for i in range(n):
    arr.append(int(input()))

answer = 0

for i in range(1,n):
    res = 0
    for j in range(i):
        if arr[i] > arr[j]:
            res = max(res,dp[j])
    dp[i] = res + 1

print(n-max(dp))
