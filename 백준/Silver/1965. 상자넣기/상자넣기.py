n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
for i in range(1,n):
    res = 0
    for j in range(i):
        if arr[j] < arr[i]:
            res = max(dp[j],res)
    dp[i] = res+1
print(max(dp))