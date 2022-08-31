def solution(s):
    dic = dict()
    dic['('] = 1
    dic[')'] = -1
    answer = False
    res = 0
    
    for i in s:
        res += dic[i]
        if res < 0 :
            answer = False
            return answer
    
    if res == 0:
        answer = True
        return answer
    else:
        return answer
    
