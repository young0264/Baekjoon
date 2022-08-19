from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum_value = sum(queue1) + sum(queue2)
    que1 = deque(queue1)
    que2 = deque(queue2)

    sum_num = sum(queue1)
    cnt = 0
    length = len(queue1)
    while True:
        cnt += 1
        if cnt > 2*(length+1):
            if sum_num != sum_value//2:
                answer = -1
                break
        if sum_num == sum_value//2:
            break
        elif sum_num > sum_value//2:
            sum_num -= que1[0]
            que2.append(que1.popleft())
            answer += 1
        else:   #sum_num < sum_value//2
            sum_num += que2[0]
            que1.append(que2.popleft())
            answer += 1
        
    return answer