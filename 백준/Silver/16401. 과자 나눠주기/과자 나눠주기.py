import sys
def input():
    return sys.stdin.readline().rstrip()
m, n = map(int, input().split())
arr = list(sorted(map(int, input().split())))
left, right = 0, arr[-1]
answer = 0

while left <= right:
    mid = (left+right)//2
    cnt = 0
    if mid==0:
        print(0)
        exit(0)
    for i in range(n):
        cnt += (arr[i]//mid)

    if cnt >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid -1

print(answer)
