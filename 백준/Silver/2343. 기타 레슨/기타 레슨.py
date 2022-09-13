import sys
n, m = map(int,input().split())
arr = list(map(int,input().split()))
left, right  = 1, sum(arr)
answer = sys.maxsize
max_value = max(arr)
while left <= right:

    mid = (left+right)//2
    res,cnt = 0,0

    for i in range(n):
        # print("12312",left,mid,right)
        if res+arr[i] <= mid:
           res +=  arr[i]
        else:
            res = arr[i]
            cnt += 1
            if cnt == m:
                # print("i",i)
                left = mid+1
                break

    else:
        right = mid-1
        answer = min(answer,mid)
    # print(left,right,mid)
    answer = min(answer,mid)
        # print(12312,answer)
if left<max_value:
    print(max_value)
    exit(0)
print(left)
# print(answer)
