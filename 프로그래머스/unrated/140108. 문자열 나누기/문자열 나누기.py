def solution(s):
    answer = 0
    now = ''
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if cnt1 and cnt1 == cnt2:
            answer += 1
            now = i
            cnt1 = 0
            cnt2 = 0
            
        if not cnt1:
            now = i
            cnt1 += 1
        elif now == i:
            cnt1 += 1
        else: #now하고 다르면
            cnt2 += 1
            
    
    return answer+1