#범위안에 있고
import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
arr=[]
dp = [0]*(n+1)   #dp[-1]이 정답
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    if arr[i][0] + i <= n:
        dp[i+arr[i][0]] = max((arr[i][1]+dp[i]), dp[i+arr[i][0]])
    dp[i+1] = max(dp[i],dp[i+1])
print(max(dp))

