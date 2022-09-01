import sys
def solution(s):
    s = list(s)
    answer = sys.maxsize
    length = len(s)
    if length == 1:
        return 1
    for size in range(1,(length//2)+1):
        res = []
        cnt = 1
        box= s[:size]
        for i in range(size,length,size):
            # print("i,cnt,s[i:i+size]",i,cnt,s[i:i+size])
            # print("s[i:i+size]",s[i:i+size])
            if s[i:i+size] == box:
                cnt += 1
            else:
                if cnt>=2:
                    res +=([str(cnt)] + box)
                else:
                    res += box
                box = s[i:i+size]
                cnt = 1
        if cnt >= 2:
            res +=([str(cnt)] + box)
        else:
            res += box
        res = ''.join(res)
        # print("res",res)
        answer = min(answer,len(res))
    
    # print("answer",answer)
    return answer