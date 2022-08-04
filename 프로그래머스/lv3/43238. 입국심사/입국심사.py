def solution(n, times):
    answer = 0
    left , right = 0,n*max(times)
    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for i in times:
            cnt += (mid//i)
        if cnt >= n:
            right = mid-1
            answer = mid
        else:
            left = mid + 1
            
    
    return answer