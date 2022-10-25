from collections import deque
def solution(s):
    answer = 0
    n = len(s)
    s = deque(s)
    # print(s)
    if n==1:
        return 0
    def isRightG(s):
        stack = []
        c1, c2, c3 = 0, 0, 0
        for i in s:
            if i =='[':
                stack.append(1)
                c1 += 1           
            elif i ==']':
                c1 -= 1
                if c1 < 0:
                    return False
                elif stack.pop() != 1:
                    return False
                
                        
            elif i =='{':
                c2 += 1
                stack.append(2)
            elif i=='}':
                c2 -= 1
                if c2 < 0:
                    return False
                elif stack.pop() != 2 :
                    return False
                
            elif i=='(':
                c3+=1
                stack.append(3)
            elif i==')':
                c3 -= 1
                if c3 < 0:
                    return False
                elif stack.pop() != 3:
                    return False

        if c1>0 or c2>0 or c3>0:
            return False
        return True
                
            
    for i in range(n):
        s.append(s.popleft())
        # print("s",s)
        if isRightG(s):
            answer += 1
    
    
    return answer