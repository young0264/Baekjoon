def solution(k, score):
    answer = []
    arr = []
    for i in score:
        arr.append(i)
        arr.sort(reverse=True)
        # print(arr)
        if len(arr) < k:
            answer.append(arr[-1])
        else:
            answer.append(arr[k-1])
            
    
    
    
    return answer