
dp = [0]*(10001)
dp[1],dp[2] = 1,1

for i in range(3,10001):
    dp[i] = dp[i-1]+dp[i-2]
t = int(input())
cnt = 1
for i in range(t):
    p,q = map(int,input().split())
    res = dp[p]%q
    print("Case #"+str(cnt)+":",res)
    cnt+=1
