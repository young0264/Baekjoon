import math
def solution(number, limit, power):
    
    def find(num):
        cnt = 0
        for i in range(1, int(math.sqrt(num))+1):
            if not num%i:
                cnt += 2
        if num == int(math.sqrt(num))**2:
            cnt -= 1
        return cnt
    
    answer = 0
    
    for i in range(1,number+1):
        res = find(i)

        if res > limit:
            answer += power
        else:
            answer += res
    
    return answer