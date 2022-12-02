#bfs, dp
import sys
a,k = map(int,input().split())
dp = [sys.maxsize]*1000001

# for i in range(1,1000001):
#     dp[i] = i-1
dp[a] = 0
for i in range(a,1000000):

    dp[i+1] = min(dp[i+1],dp[i]+1)
    if i*2 < 1000001:
        dp[i*2] = min(dp[i*2],dp[i]+1)
print(dp[k]-dp[a])
# print(dp[k], dp[a])