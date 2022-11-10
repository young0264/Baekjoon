n = int(input())
k = int(input())

left = 1
right = n**2

while left < right:
    cnt = 0
    mid = (left+right)//2
    # print(left, mid, right)

    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        right = mid
    else:
        left = mid+1
    # print("cnt : ", cnt)
print(left)
# print(mid)
