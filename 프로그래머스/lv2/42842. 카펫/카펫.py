def solution(brown, yellow):
    answer = []
    
    
    def find_brown(r,c):
        res = 0
        res+=r*2
        res+=2*(c-2)
        return res
    
    def find_yellow(r,c):
        res = 0
        res += (r-2)*(c-2)
        return res
    
    for i in range(3,2500):
        for j in range(3,2500):
            brown2 = find_brown(i,j)
            yellow2 = find_yellow(i,j)
            if brown==brown2 and yellow == yellow2:
                answer += [j,i]
                return answer
    
    
    return answer