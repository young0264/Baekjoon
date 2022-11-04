# 9
# 100 1 5 1 100 100 100 100 100
import sys

n = int(input())
P =[0]+ list(map(int,input().split()))
dp = [i for i in P]

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i], dp[i-j]+P[j])
print(dp[-1])