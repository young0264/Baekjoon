#1 : 상근, 2:창영이 마지막을 가져가는거 -> 1=창영win, 2=상근win
n = int(input())

dp = [0]*(1001)
dp[1],dp[2],dp[3],dp[4] = 1,2,1,2

for i in range(5,1001):
    if dp[i-1] == 1 or dp[i-3]==1 or dp[i-4]==1: #상근이 다 가져간거
        dp[i] = 2
    else: #창영이 다 가져간거
        dp[i] = 1

if dp[n]==2:
    print("SK")
else:
    print("CY")
