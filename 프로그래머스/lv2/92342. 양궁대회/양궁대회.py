from itertools import combinations_with_replacement
def solution(n, apeach_arr):
    answer = []
    cha_value = 0
    arr = [i for i in range(11)]
    for  lion_info in combinations_with_replacement(arr,n):
        lion_arr = [0]*11
        lion_cnt , apeach_cnt = 0,0
        for i in lion_info:
            lion_arr[i] += 1

        for i in range(11): #[0 2 2 0 1 0 0 0 0 0 0 0 ]
            if lion_arr[i] > apeach_arr[i]:
                lion_cnt += 10-i
            elif lion_arr[i] == apeach_arr[i] == 0:
                continue
            elif lion_arr[i] <= apeach_arr[i]:
                apeach_cnt += 10-i
                
        flag = 0
        if lion_cnt > apeach_cnt:
            if cha_value < lion_cnt-apeach_cnt:
                cha_value = lion_cnt-apeach_cnt
                answer = lion_arr
            elif cha_value == lion_cnt-apeach_cnt   :
                for i in range(10,-1,-1):
                    if lion_arr[i] == answer[i]==0:
                        continue
                    elif lion_arr[i] > answer[i]:
                        answer = lion_arr
                        break
                    else:
                        break

    if not answer :
        answer.append(-1)
        
    return answer











