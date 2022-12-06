import sys

n, k = map(int,input().split())
arr = [0]+list(map(int,input().split()))
dp = [[0]*(n+1) for _ in range(k+1)]

#값이 홀수이면 현재 숫자를 제외하고(n-1), 숫자 한개를 덜 제외한 값(k-1)

for i in range(1,n+1):
    if arr[i]%2==0:
        dp[0][i] = dp[0][i-1]+1
dp[0][0] = 0
for i in range(1,k+1):
    for j in range(1,n+1):
        if arr[j]%2 == 0:   #짝수이면
            dp[i][j] = dp[i][j-1]+1
        else:   #홀수이면
            dp[i][j] = dp[i-1][j-1]
answer = -1
# for i in dp:
#     answer = max(answer,max(i))
# for i in dp:
#     print(i)
# print(answer)
print(max(dp[k]))