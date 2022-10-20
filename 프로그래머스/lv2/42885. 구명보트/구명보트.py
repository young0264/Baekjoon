#양쪽으로 빼는 (바라보는) 개념

from collections import deque

def solution(people, limit):
    answer = 0
    now= 0
    people.sort()
    # print(people)
    que = deque(people)
    while que:
        if len(que) == 1:
            answer += 1
            break
        if que[0] + que[-1] <= limit:
            que.pop()
            que.popleft()
        else:
            que.pop()
        answer += 1

    return answer