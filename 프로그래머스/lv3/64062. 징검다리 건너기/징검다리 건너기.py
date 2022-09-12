def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    length = len(stones)
    arr = [1]*length
    while left<=right:
        mid = (left+right)//2
        cnt = 0
        for i in range(length):
            if stones[i] <= mid:
                cnt += 1
                if cnt > k: #####등호
                    right = mid-1
                    break
                elif cnt==k:
                    right = mid-1
                    # answer = mid
                    # print("mid",mid)
                    # return mid
                    break
            else:
                cnt = 0
        else : left = mid+1
        #
    # print("ans",answer)
    return left