def solution(d, budget):
    d.sort()
    answer = 0
    
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
        
    
    return answer