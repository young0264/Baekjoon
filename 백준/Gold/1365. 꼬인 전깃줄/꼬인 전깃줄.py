from bisect import bisect_left

n = int(input())
arr = list(map(int,input().split()))
dp=[arr[0]]
#연속으로 증가하지 않는 수열의 countx
# 잘라내야할게 왜 최소갯수지
# 3,5,1,4,6,7,8,2
for i in range(1,len(arr)):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        k = bisect_left(dp,arr[i])
        dp[k] = arr[i]
print(n-len(dp))

