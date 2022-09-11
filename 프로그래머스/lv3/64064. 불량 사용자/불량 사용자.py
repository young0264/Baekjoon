from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    length = len(banned_id)
    ans_arr = []
    for permu in permutations(user_id,length):
        permu = list(permu)
        visited = [0]*length
        # print("permu",permu)
        flag = 0
        for i in range(length): #banned_id
            if len(banned_id[i]) == len(permu[i]):
                # print((banned_id[i]),(permu[i]))
                for j in range(len(banned_id[i])):
                    if banned_id[i][j] !='*' and banned_id[i][j] != permu[i][j]:
                        flag = 1
            else:   #길이가 같지 않아서 조건 성립이 안될때
                flag = 1
                break
        if not flag :
            res = ''
            # ans_arr.append(sorted(permu))
            for i in sorted(permu):
                res+=i
            ans_arr.append(res)
            
    answer = (len(list(set(ans_arr))))
    return answer



