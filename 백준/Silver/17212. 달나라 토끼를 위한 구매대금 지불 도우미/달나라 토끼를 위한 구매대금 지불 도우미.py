n = int(input())
dp= [0]+[i for i in range(1,n+1)]
coin = [2,5,7]
#2,5,7
# dp[k+coin[i]] = min(dp[k+coin[i]],dp[k]+1)
for i in range(3):
    idx = 0
    while idx+coin[i]<=n:
        dp[idx+coin[i]] = min(dp[idx+coin[i]],dp[idx]+1)
        idx += 1
print(dp[-1])