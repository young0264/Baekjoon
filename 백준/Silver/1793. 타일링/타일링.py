dp = [0]*251
dp[0],dp[1], dp[2] = 1,1,3
for i in range(3,251):
    dp[i] = 2*dp[i-2] + dp[i-1]
arr = []
while True:
    try:
        n = int(input())
        print(dp[n])
    except :
        break




