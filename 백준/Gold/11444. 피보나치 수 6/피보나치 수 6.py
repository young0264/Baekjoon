#60
import sys
sys.setrecursionlimit(10*6)
n = int(input())
mod = 1000000007
dp = dict()
input = sys.stdin.readline
def dfs(num):
    if dp.get(num):
        return dp[num]
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    elif num ==3 :
        return 2
    else:
        k = num//2
        if num%2 == 0: #짝
            dp[k+1] = dfs(k+1)%mod
            dp[k-1] = dfs(k-1)%mod
            # dp[num] =  dfs(k)%mod * (dfs(k-1)%mod + dfs(k+1)%mod)
            dp[num] = dp[k+1]**2%mod - dp[k-1]**2%mod
            return dp[num]
        else: #홀
            k=k+1
            # return dfs(k-2)*dfs(k)%mod + dfs(k-1)*dfs(k+1)%mod
            dp[k] = dfs(k)%mod
            dp[k-1] = dfs(k-1)%mod
            dp[num] = dp[k]**2%mod + dp[k-1]**2%mod
            return dp[num]
res= dfs(n)
print(res%mod)


