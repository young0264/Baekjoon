import sys
def input():
    return sys.stdin.readline().rstrip()
n, k = map(int, input().split())
arr = []
for _ in range(n):
    m = int(input())
    arr.append(m)
left, right = 1, max(arr)
answer = 0
while left <= right:
    cnt = 0
    mid = (left+right)//2

    for i in arr:
        cnt += i//mid

    if cnt >= k:
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(answer)
