import sys
def input():
    return sys.stdin.readline().rstrip()

s,c = map(int, input().split())
answer = 0
leeks = []
for i in range(s):
    leek = int(input())
    leeks.append(leek)
left,right = 1,max(leeks)

while left<=right:
    mid = (left+right)//2
    # print(left,right,mid)
    cnt = 0
    for leek in leeks:
        cnt += leek//mid
    if cnt < c:
        right = mid-1
    else:
        left = mid+1
        if cnt > c:
            answer = sum(leeks) - c*mid
        else:
            answer = sum(leeks) - cnt*mid
print(answer)
