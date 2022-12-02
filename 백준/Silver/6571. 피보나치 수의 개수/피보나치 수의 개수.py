dp = [0]*10001
dp[1],dp[2] = 1,2
for i in range(3,10001):
    dp[i] = dp[i-1]+dp[i-2]
while True:
    a,b = map(int,input().split())
    count = 0
    if a==0 and b==0:
        break
    for i in range(1,10001):
        if a<= dp[i] <=b:
            count += 1
        elif dp[i] > b:
            break
    print(count)

