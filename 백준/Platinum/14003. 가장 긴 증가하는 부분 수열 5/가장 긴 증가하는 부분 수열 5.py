from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))
dp =[arr[0]]
new_arr = []
answer = []
max_value = 0
for i in range(n):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
        new_arr.append((len(dp)-1,arr[i])) #len(idx),value
    else:
        k = bisect_left(dp,arr[i])
        dp[k] = arr[i]
        new_arr.append((k,arr[i]))
print(len(dp))
length = len(dp)-1
for i in range(len(new_arr)-1,-1,-1):
    if new_arr[i][0]==length:
        answer.append(new_arr[i][1])
        length -=1
print(*reversed(answer))
