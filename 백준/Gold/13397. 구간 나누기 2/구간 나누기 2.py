import sys
n,m = map(int,input().split())
arr = list(map(int,input().split()))
left , right = 0,max(arr)
answer = sys.maxsize

def find(mid):
    min_value,max_value = sys.maxsize,-sys.maxsize
    sec_cnt = 1
    for i in range(n):
        min_value = min(min_value,arr[i])
        max_value = max(max_value,arr[i])
        if (max_value - min_value) > mid:
            sec_cnt +=1
            min_value = max_value = arr[i]
    if sec_cnt <= m:
        return True
    else:
        return False


while left<=right:
    mid = (left+right)//2
    # print(left,mid,right)
    if find(mid):
        answer = min(answer,mid)
        right = mid-1
    else:
        left = mid+1

print(answer)

