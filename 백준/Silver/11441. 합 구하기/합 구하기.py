import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]*n
answer = []

for i in range(1,n):
    dp[i] = arr[i] + dp[i-1]
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    if a>1:
        answer.append(dp[b-1]-dp[a-2])
    else:
        answer.append(dp[b-1])
for i in answer:
    print(i)