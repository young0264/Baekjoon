#O(N)이 아니라 O(NlongN) 아아
#10 20 10 30 20 50
#10,1,2,3,4,50
from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))
dp =[0]
dp[0] = arr[0]
for i in range(1,len(arr)):
    k = bisect_left(dp,arr[i])
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        dp[k]=arr[i]

print(len(dp))