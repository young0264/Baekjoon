import math,sys
n = int(input())
dp = [i for i in range(n+1)]
dp[1] = 1
for i in range(1,n+1):
    for j in range(1,i):
        if j**2 > i:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
        # dp[i] = min(dp[i],dp[i%(j**2)]+1)

        # res = int(math.sqrt(i))**2
        # mod = i//res
        # m = i%res
        # dp[i] = mod+dp[m]

# print(dp)
print(dp[n])
# print(math.sqrt(n))
# print(27**2)
