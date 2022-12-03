#가장 긴 감소부분수열
#반례 : arr : [15,17]
n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if arr[j] <= arr[i]:
            continue
        else:
            dp[i] = max(dp[i],dp[j]+1)
# print(dp)
print(n-max(dp))