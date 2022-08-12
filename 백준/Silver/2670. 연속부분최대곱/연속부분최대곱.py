n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))

dp1 = [arr[0]]*n

dp = [i for i in arr]

for i in range(1,n):
    if dp[i-1]*arr[i] >= arr[i]:
        dp[i] = dp[i-1]*arr[i]
    else:
        dp[i] = arr[i]
answer = format(max(dp), "1.3f")
print(answer)

